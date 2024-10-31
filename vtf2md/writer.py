from typing import List

from pytablewriter import MarkdownTableWriter
from pytablewriter.style import Style


def write_markdown_table(sorted_variables: List[List[str]]) -> None:
    MarkdownTableWriter(
        headers=["Name", "Type", "Description", "Default", "Required", "Sensitive"],
        value_matrix=sorted_variables,
        margin=1,
        column_styles=[
            Style(align="left"),
            Style(align="left"),
            Style(align="left"),
            Style(align="left"),
            Style(align="left"),
            Style(align="left"),
        ],
    ).write_table()
