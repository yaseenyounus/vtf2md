#!/bin/sh

if ! command -v pip &> /dev/null; then
    echo "pip isn't installed. Please install Python and try again. Exiting..."
    exit 1
fi

pip install -q poetry

poetry install
poetry run python3 vtf2md/main.py "$@"
