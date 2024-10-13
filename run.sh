#!/bin/sh

if ! command -v poetry &> /dev/null; then
    pip install -q poetry
fi

poetry install -q
poetry run python3 vtf2md/main.py "$@"
