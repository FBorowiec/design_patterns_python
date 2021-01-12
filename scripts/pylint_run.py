import logging
import os
import sys
from pylint.lint import Run

if __name__ == "__main__":
    threshold = 10.0
    target_dir = sys.argv[1]

    py_files = []
    for dirpath, dirnames, filenames in os.walk(target_dir):
        for filename in [f for f in filenames if f.endswith(".py")]:
            py_files.append(os.path.join(dirpath, filename))

    results = []
    total_score = 0
    for f in py_files:
        pylint_opts = [f, "--disable", "C0103,C0114,C0115,C0116,E0401,E0611,F0010"]
        print("Module: {}".format(f.split("/")[-1]))
        result = Run(pylint_opts, do_exit=False)
        results.append(result)
        total_score += 10

    final_score = sum(r.linter.stats["global_note"] for r in results)
    score = final_score / total_score * 10.0

    if score >= threshold:
        message = (
            "PyLint Passed | " "Score: {} | " "Threshold: {} ".format(score, threshold)
        )

        logging.info(message)
        sys.exit(0)

    else:
        message = (
            "PyLint Failed | " "Score: {} | " "Threshold: {} ".format(score, threshold)
        )

        logging.error(message)
        raise Exception(message)
