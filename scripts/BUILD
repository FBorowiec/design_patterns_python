load("@rules_python//python:defs.bzl", "py_binary")
load("@design_patterns_deps//:requirements.bzl", "requirement")
load("@com_github_bazelbuild_buildtools//buildifier:def.bzl", "buildifier")

py_binary(
    name = "black",
    srcs = ["black_run.py"],
    main = "black_run.py",
    visibility = ["//visibility:public"],
    deps = [requirement("black")],
)

py_binary(
    name = "black_check",
    srcs = ["black_run.py"],
    args = ["--check --diff"],
    main = "black_run.py",
    visibility = ["//visibility:public"],
    deps = [requirement("black")],
)

py_binary(
    name = "pylint",
    srcs = ["pylint_run.py"],
    main = "pylint_run.py",
    visibility = ["//visibility:public"],
    deps = [requirement("pylint")],
)

buildifier(
    name = "buildifier",
)

buildifier(
    name = "buildifier_check",
    lint_mode = "warn",
    mode = "check",
)
