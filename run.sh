#!/bin/sh

# Install Poetry dependencies
poetry install

# Run the Python script and pass all arguments
poetry run python vtf2md/main.py "$@"
