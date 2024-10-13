import hcl2
from pytablewriter import MarkdownTableWriter
from pytablewriter.style import Style


md_table = []

with open("variables.tf", "r") as file:
    tf_dict = hcl2.load(file)

for x in tf_dict["variable"]:
    for key, value in x.items():
        name = key
        var_type = value.get("type", None).strip("${}")
        description = value.get("description", None)
        default = value.get("default", None)

        md_table.append(
            [name, var_type, description, default, "False" if default else "True"]
        )

        print(name, var_type, description, default)

print(md_table)


writer = MarkdownTableWriter(
    headers=["Name", "Type", "Description", "Default", "Required"],
    value_matrix=md_table,
    margin=1,
    column_styles=[
        Style(align="left"),
        Style(align="left"),
        Style(align="left"),
        Style(align="left"),
        Style(align="left"),
    ],
)

writer.write_table()
