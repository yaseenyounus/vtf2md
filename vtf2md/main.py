import hcl2

with open("variables.tf", 'r') as file:
    tf_dict = hcl2.load(file)

for x in tf_dict["variable"]:
    for key, value in x.items():
        name = key
        var_type = value.get("type", None).strip("${}")
        description = value.get("description", None)
        default = value.get("default", None)

        print(name, var_type,  description, default)
