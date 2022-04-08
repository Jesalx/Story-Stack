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


def parse_id(id_str: str) -> int:
    """
    Takes a string and returns the integer in s, or 0 if s is not an integer
    or below 0.
    """
    try:
        return max(int(id_str), 0)
    except ValueError:
        return 0
