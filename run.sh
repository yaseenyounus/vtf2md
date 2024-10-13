#!/bin/sh

poetry install
poetry run python3 vtf2md/main.py "$@"
