#!/usr/bin/env bash

bazel run //scripts:pycoverage -- $(bazel info --show_make_env workspace)
