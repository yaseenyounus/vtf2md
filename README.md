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

### Default path

If a `variables.tf` file is in the same directory as the `run.sh` script, it can be called without any arguments.

```sh
./run.sh
```

Otherwise... ⬇️

### Passing a Terraform variables file path

```sh
./run.sh --path tests/variables.tf
```

or `-p` for short

```sh
./run.sh -p tests/variables.tf
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

```sh
./run.sh -p tests/variables.tf
```

### Output

| Name            | Type         | Description                                     | Default                        | Required |
| --------------- | ------------ | ----------------------------------------------- | ------------------------------ | -------- |
| vpc_cidr_block  | string       | The top-level CIDR block for the VPC.           | 10.1.0.0/16                    | False    |
| cidr_blocks     | list(string) | The CIDR blocks to create the workstations in.  | ['10.1.1.0/24', '10.1.2.0/24'] | False    |
| namespace       | string       | Default namespace                               | n/a                            | True     |
| cluster_id      | string       | Id to assign the new cluster                    | n/a                            | True     |
| public_key_path | string       | Path to public key for ssh access               | ~/.ssh/id_rsa.pub              | False    |
| node_groups     | number       | Number of nodes groups to create in the cluster | 3                              | False    |

## Contributing

Feel free to open a PR!

## License

This project is licensed under the MIT License
