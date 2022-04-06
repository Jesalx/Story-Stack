"""
File containing backend functions for the processing of stories.
"""


def extract_tags(input_string: str):
    """
    Takes a string and returns a list of tags.
    """
    tags = set()
    for tag in input_string.split(","):
        tags.add(tag.strip().lower())

    return list(tags)
