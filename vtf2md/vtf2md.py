from cli import parse_cli_arguments
from extractor import extract_variables
from loader import load_terraform_files
from writer import write_markdown_table


def vtf2md():
    file_paths = parse_cli_arguments().path
    terraform_configs = load_terraform_files(file_paths)
    sorted_variables = extract_variables(terraform_configs)
    write_markdown_table(sorted_variables)


if __name__ == "__main__":
    vtf2md()
