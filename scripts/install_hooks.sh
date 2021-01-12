#!/usr/bin/env bash

echo "Installing pre-commit" && pip3 install pre-commit &>/dev/null
pre-commit --version

set -eu
toplevel=${1:-$(git rev-parse --show-toplevel)}
cd ${toplevel}

echo "Installing git hooks in ${toplevel}" && pre-commit install
echo "Running pre-commit hooks" && pre-commit run --all-files
