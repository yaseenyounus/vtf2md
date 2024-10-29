from argparse import ArgumentParser, Namespace
from os.path import abspath
from sys import exit
from typing import Any, Dict, List

from hcl2 import load
from pytablewriter import MarkdownTableWriter
from pytablewriter.style import Style

# TODO - separate into different files


def parse_cli_arguments() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument(
        "-p",
        "--path",
        action="append",
        help="Local path to your Terraform variables file (default: ./variables.tf)",
    )
    return parser.parse_args()


def load_terraform_files(file_paths: List[str]) -> List[Dict[str, Any]]:
    terraform_configs = []
    file_paths = file_paths or ["variables.tf"]

    try:
        for path in file_paths:
            path = abspath(path)
            with open(path, "r") as file:
                terraform_configs.append(load(file))
        return terraform_configs
    except FileNotFoundError:
        print(f"Error: The file '{path}' wasn't found. Try again...")
        print("Use --help or -h for options")
        exit(1)


def sort_variables_by_required(variable_list: List[List[str]]) -> List[List[str]]:
    required, optional = [], []
    for var in variable_list:
        if var[4] == "True":  # var[4] refers to the 'Required' column
            required.append(var)
        else:
            optional.append(var)
    return required + optional


def extract_variables(terraform_configs: List[Dict[str, Any]]) -> List[List[str]]:
    variable_rows = []
    for terraform_dict in terraform_configs:
        for variable_config in terraform_dict.get("variable", []):
            for name, value in variable_config.items():
                variable_type = value.get("type", "").strip("${}")
                description = value.get("description", "")
                default = value.get("default", "n/a")
                sensitive = value.get("sensitive", False)

                variable_rows.append(
                    [
                        name,
                        variable_type,
                        description,
                        default,
                        "True" if default == "n/a" else "False",
                        "True" if sensitive else "False",
                    ]
                )
    return sort_variables_by_required(variable_rows)


def write_markdown_table(sorted_variables: List[List[str]]) -> None:
    MarkdownTableWriter(
        headers=["Name", "Type", "Description", "Default", "Required", "Sensitive"],
        value_matrix=sorted_variables,
        margin=1,
        column_styles=[
            Style(align="left"),
            Style(align="left"),
            Style(align="left"),
            Style(align="left"),
            Style(align="left"),
            Style(align="left"),
        ],
    ).write_table()


def main():
    file_paths = parse_cli_arguments().path
    terraform_configs = load_terraform_files(file_paths)
    sorted_variables = extract_variables(terraform_configs)
    write_markdown_table(sorted_variables)


if __name__ == "__main__":
    main()
