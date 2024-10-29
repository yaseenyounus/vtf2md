@echo off

REM Install Poetry dependencies
call poetry install

REM Run the Python script and pass all arguments
call poetry run python vtf2md\main.py %*
