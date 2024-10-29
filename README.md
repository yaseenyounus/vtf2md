# variables.tf 2 Markdown (`vtf2md v0.2.0`)

## Overview

This Python script streamlines Terraform module documentation by extracting variables and generating Markdown tables, saving time and effort.

## Requirements

- Python 3.12+
- [Poetry](https://python-poetry.org/docs/#installation)

## Installation

### Clone the repo

```sh
git clone https://github.com/yaseenyounus/vtf2md.git
cd vtf2md
```

### Set up Poetry

```sh
pip install poetry
```

_You may need to restart your terminal after installing `poetry`_

## Usage

You can use the `run.sh` (Mac / Linux) or `run.bat` (Windows) script to install the Python dependencies with Poetry and run the script on your behalf.

### Default path

If a `variables.tf` file is in the same directory as the `run.sh` / `run.bat` script, it can be called without any arguments.

#### Mac / Linux

```sh
./run.sh
```

#### Windows

```batch
./run.bat
```

Otherwise... ⬇️

### Using a single Terraform file

#### Mac / Linux

```sh
./run.sh --path tests/variables.tf

# or `-p` for short
./run.sh -p tests/variables.tf
```

#### Windows

```batch
./run.bat --path tests/variables.tf

REM or `-p` for short
./run.bat -p tests/variables.tf
```

### Using multiple Terraform files

#### Mac / Linux

```sh
./run.sh --path tests/variables.tf --path tests/variables_2.tf

# shorthand syntax
./run.sh -p tests/variables.tf -p tests/variables_2.tf
```

#### Windows

```batch
./run.bat --path tests/variables.tf --path tests/variables_2.tf

REM shorthand syntax
./run.bat -p tests/variables.tf -p tests/variables_2.tf
```

## Example

### `tests/variables.tf` file

```terraform
variable "vpc_cidr_block" {
  type = string
  description = "The top-level CIDR block for the VPC."
  default     = "10.1.0.0/16"
}

variable "cidr_blocks" {
  type = list(string)
  description = "The CIDR blocks to create the workstations in."
  default     = ["10.1.1.0/24", "10.1.2.0/24"]
}

variable "namespace" {
  type = string
  description = "Default namespace"
}

variable "cluster_id" {
  type = string
  description = "Id to assign the new cluster"
}

variable "public_key_path" {
  type = string
  description = "Path to public key for ssh access"
  default     = "~/.ssh/id_rsa.pub"
}

variable "node_groups" {
  type = number
  description = "Number of nodes groups to create in the cluster"
  default     = 3
}
```

### Run

#### Mac / Linux

```sh
./run.sh -p tests/variables.tf
```

#### Windows

```batch
./run.bat -p tests/variables.tf
```

### Output

| Name            | Type         | Description                                     | Default                        | Required | Sensitive |
| --------------- | ------------ | ----------------------------------------------- | ------------------------------ | -------- | --------- |
| namespace       | string       | Default namespace                               | n/a                            | True     | False     |
| cluster_id      | string       | Id to assign the new cluster                    | n/a                            | True     | False     |
| vpc_cidr_block  | string       | The top-level CIDR block for the VPC.           | 10.1.0.0/16                    | False    | False     |
| cidr_blocks     | list(string) | The CIDR blocks to create the workstations in.  | ['10.1.1.0/24', '10.1.2.0/24'] | False    | False     |
| public_key_path | string       | Path to public key for ssh access               | ~/.ssh/id_rsa.pub              | False    | False     |
| node_groups     | number       | Number of nodes groups to create in the cluster | 3                              | False    | False     |

## Contributing

- Fork this repository
- Make your changes
- Open a Pull Request

## License

This project is licensed under the [MIT License](https://github.com/yaseenyounus/vtf2md/blob/main/LICENSE)
