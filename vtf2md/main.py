import hcl2

with open("variables.tf", 'r') as file:
    tf_dict = hcl2.load(file)

for x in tf_dict["variable"]:
    for key, value in x.items():
        name = key
        description = value.get("description", None)
        default = value.get("default", None)

        print(name, description, default)
