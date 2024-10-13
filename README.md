# `variables.tf` 2 Markdown (vtf2md)

## Overview

This Python script takes a Terraform `variables.tf` file as input and outputs the extracted details in a markdown table, thereby streamlining the Terraform module documentation process.

## Requirements

- `Python` 3.12+
- [`Poetry`](https://python-poetry.org/docs/#installation)

## Installation

Clone the repo

```sh
git clone https://github.com/yaseenyounus/vtf2md.git
cd vtf2md
```

Install Poetry if it's not already installed

```sh
curl -sSL https://install.python-poetry.org | python3 -
```

or if you have `brew` installed on Mac

```sh
brew install poetry
```

## Usage

You can use the `run.sh` script to install the Python dependencies with Poetry and then run the program.

```sh
./run.sh vtf2md/main.py --path tests/variables.tf
```

or `-p` for short

```sh
./run.sh vtf2md/main.py -p tests/variables.tf
```
