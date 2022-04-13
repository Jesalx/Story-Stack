"""
Module containing backend functions for the processing search queries.
"""

from models import db, Account, Tag, Story
from story import parse_id


def search_db(query: str) -> list:
    tokens = get_query_tokens(query)

    matching_stories = set()

    for token in tokens:
        # First, we'll search the tags for this token and add
        # the stories related to that tag
        tag_obj = Tag.query.filter_by(name=token).first()
        if tag_obj:
            for story in tag_obj.stories:
                matching_stories.add(story)

        story_id = parse_id(token)
        if story_id != 0:
            story_obj = Story.query.filter_by(id=story_id).first()
            if story_obj:
                matching_stories.add(story_obj)

    return list(matching_stories)


def get_query_tokens(query: str) -> list:
    """
    Takes a query string and returns a list of tokens.
    """
    tokens = set()
    for token in query.split(" "):
        cleaned_token = token.strip().lower()
        tokens.add(cleaned_token)

    if "" in tokens:
        tokens.remove("")

    return tokens
