from typing import Any, Dict, List


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
