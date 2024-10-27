from argparse import ArgumentParser
from hcl2 import load
from pytablewriter import MarkdownTableWriter
from pytablewriter.style import Style
from sys import exit
from typing import List
from itertools import chain

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


def load_terraform_files(paths: List[str]) -> List[dict]:
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


def required_to_beginning_list(nested_list: list) -> list:
    required = [x for x in nested_list if "True" in x]
    optional = [x for x in nested_list if "True" not in x]
    return required + optional


def extract_values(values: dict) -> list:
    md_table = []
    for x in values["variable"]:
        for key, value in x.items():
            name = key
            var_type = value.get("type", "").strip("${}")
            description = value.get("description", "")
            default = value.get("default", "n/a")

            md_table.append(
                [
                    name,
                    var_type,
                    description,
                    default,
                    "True" if default == "n/a" else "False",
                ]
            )
    return required_to_beginning_list(md_table)


def generate_md_table(values: list) -> None:
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
    print(terraform_hcl_list)

    # markdown_list = extract_values(terraform_dict)

    # tf_var_list = []
    # for tf_dict in tf_rendered_list:
    #     tf_var_list.append(extract_values(tf_dict))

    # print(tf_var_list)

    # tf_var_combined_list = list(chain(*tf_var_list))
    # print(tf_var_combined_list)

    # sorted_tf_vars = required_to_beginning_list(tf_var_combined_list)
    # print(sorted_tf_vars)

    # generate_md_table(sorted_tf_vars)


if __name__ == "__main__":
    main()
