import logging
import unittest
import coverage
import sys
from pathlib import Path
import collections

PycoverageResult = collections.namedtuple("PycoverageResult", "runs errors failures")


def check_coverage(*deps):
    cov = coverage.Coverage(branch=True, omit="bazel-*")
    cov.start()

    loader = unittest.TestLoader()

    all_tests_suite = unittest.TestSuite()

    for dep in deps:
        if ":" in dep:
            target_name_of_label = dep.rpartition(":")[2]
        else:
            target_name_of_label = dep.rpartition("/")[2]

        paths = list(Path(".").glob(f"**/{target_name_of_label}"))

        if len(paths) == 0:
            logging.fatal(
                f"Couldn't find {target_name_of_label} below {Path('.').as_posix()}. Unexpected"
            )
            sys.exit(1)

        suite = loader.discover(start_dir=paths[0].parent, pattern="*test*.py")
        all_tests_suite.addTests(suite)

    runner = unittest.TextTestRunner()
    result = runner.run(all_tests_suite)

    cov.stop()
    cov.save()

    cov.html_report(directory="pycoverage_html")
    cov.xml_report(outfile="pycoverage.xml")

    pycoverage_results = PycoverageResult(
        runs=result.testsRun, errors=len(result.errors), failures=len(result.failures)
    )

    cov.report()

    logging.info("Number of runs: %s", pycoverage_results.runs)
    logging.info("Number of errors: %s", pycoverage_results.errors)
    logging.info("Number of failures: %s", pycoverage_results.failures)

    if len(result.failures) > 0:
        logging.error("At least one test failed")
        sys.exit(1)

    return cov, pycoverage_results


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.getLogger("unittest").setLevel(logging.FATAL)
    check_coverage(*sys.argv[1:])
