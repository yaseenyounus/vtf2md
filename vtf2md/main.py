from argparse import ArgumentParser
from hcl2 import load
from pytablewriter import MarkdownTableWriter
from pytablewriter.style import Style


def load_tf_file(file_path: str) -> dict:
    with open(file_path, "r") as file:
        return load(file)


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

    return md_table


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
    parser = ArgumentParser()
    parser.add_argument(
        "-p",
        "--path",
        required=True,
        help="Local path to your Terraform variables file",
    )
    args = parser.parse_args()

    print(args)
    print(args.path)

    # terraform_dict = load_tf_file("variables.tf")
    # markdown_list = extract_values(terraform_dict)
    # generate_md_table(markdown_list)


if __name__ == "__main__":
    main()
