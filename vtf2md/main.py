from argparse import ArgumentParser
from hcl2 import load
from pytablewriter import MarkdownTableWriter
from pytablewriter.style import Style
from sys import exit
from typing import Any, Dict, List

# TODO - set default path with [] logic


def cli_arguments() -> List[str]:
    parser = ArgumentParser()
    parser.add_argument(
        "-p",
        "--path",
        default=[],
        action="append",
        help="Local path to your Terraform variables file (default: ./variables.tf)",
    )
    return parser.parse_args()


def load_terraform_files(paths: List[str]) -> List[Dict[str, Any]]:
    try:
        terraform_hcl_list = []
        for path in paths:
            with open(path, "r") as file:
                terraform_hcl_list.append(load(file))
        return terraform_hcl_list
    except FileNotFoundError:
        print(f"Error: The file '{path}' wasn't found. Try again...")
        print("Use --help or -h for options")
        exit(1)


def required_to_beginning_list(nested_list: List[List[str]]) -> List[List[str]]:
    required = [x for x in nested_list if "True" in x]
    optional = [x for x in nested_list if "True" not in x]
    return required + optional


def extract_values(terraform_hcl_list: List[Dict[str, Any]]) -> List[List[str]]:
    markdown_table = []
    for terraform_dict in terraform_hcl_list:
        for terraform_var_dict in terraform_dict.get("variable", []):
            for name, value in terraform_var_dict.items():
                var_type = value.get("type", "").strip("${}")
                description = value.get("description", "")
                default = value.get("default", "n/a")
                sensitive = value.get("sensitive", False)

                markdown_table.append(
                    [
                        name,
                        var_type,
                        description,
                        default,
                        "True" if default == "n/a" else "False",
                        "True" if sensitive else "False",
                    ]
                )
    return required_to_beginning_list(markdown_table)


def generate_markdown_table(values: list) -> None:
    MarkdownTableWriter(
        headers=["Name", "Type", "Description", "Default", "Required"],
        value_matrix=values,
        margin=1,
        column_styles=[
            Style(align="left"),
            Style(align="left"),
            Style(align="left"),
            Style(align="left"),
            Style(align="left"),
        ],
    ).write_table()


def main():
    paths = cli_arguments().path
    print(paths)

    terraform_hcl_list = load_terraform_files(paths)

    markdown_list = extract_values(terraform_hcl_list)
    print(markdown_list)

    generate_markdown_table(markdown_list)


if __name__ == "__main__":
    main()
