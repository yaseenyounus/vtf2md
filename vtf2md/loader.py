from os.path import abspath
from sys import exit
from typing import Any, Dict, List

from hcl2 import load


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
