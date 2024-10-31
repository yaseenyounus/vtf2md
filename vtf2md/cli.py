from argparse import ArgumentParser, Namespace


def parse_cli_arguments() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument(
        "-p",
        "--path",
        action="append",
        help="Local path to your Terraform variables file (default: ./variables.tf)",
    )
    return parser.parse_args()
