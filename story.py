"""
File containing backend functions for the processing of stories.
"""


def extract_tags(input_string: str) -> set:
    """
    Takes a string and returns a set of tags.
    """
    tags = set()
    for tag in input_string.split(","):
        cleaned_tag = tag.strip().lower()
        tags.add(cleaned_tag)

    if "" in tags:
        tags.remove("")

    return tags
