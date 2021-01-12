#!/usr/bin/env bash

bazel run //scripts:pylint -- $(bazel info --show_make_env workspace)
