"""
Module containing backend functions for the processing search queries.
"""

from models import Account, Tag, Story
from story import parse_id


def search_db(query: str) -> list:
    """
    Takes a query string and returns a list of Story objects that
    match any of the tokens in the query.

    Args:
        query (str): A string representing a search query.

    Returns:
        list: A list of Story objects that match the query.
    """
    tokens = get_query_tokens(query)
    matching_stories = set()

    for token in tokens:
        # Searching tags
        tag_obj = Tag.query.filter_by(name=token).first()
        if tag_obj:
            for story in tag_obj.stories:
                matching_stories.add(story)

        # Searching story ids
        story_id = parse_id(token)
        if story_id != 0:
            story_obj = Story.query.filter_by(id=story_id).first()
            if story_obj:
                matching_stories.add(story_obj)

        # Searching usernames
        account_obj = Account.query.filter_by(username=token).first()
        if account_obj:
            user_stories = Story.query.filter_by(userid=account_obj.id).all()
            for story in user_stories:
                matching_stories.add(story)

    return list(matching_stories)


def search_children(story_id: int) -> tuple:
    """
    Takes a story id and returns a tuple containing child titles, child text,
    and child ids.

    Args:
        story_id (int): An integer representing an existing story id.

    Returns:
        tuple: A tuple containing child titles, child text, and child ids.
    """
    child_titles = []
    child_text = []
    child_ids = []
    children = Story.query.filter_by(parent=story_id).all()
    print(children)
    if children:
        for child in children:
            child_titles.append(child.title)
            child_text.append(child.text)
            child_ids.append(child.id)
    print(child_titles)
    return child_titles, child_text, child_ids


def get_query_tokens(query: str) -> set:
    """
    Takes a query string and returns a list of tokens.

    Args:
        query (str): A whitespace separated string.

    Returns:
        set: A set of lowercased and whitespace stripped words.
    """
    tokens = set()
    for token in query.split(" "):
        cleaned_token = token.strip().lower()
        tokens.add(cleaned_token)

    if "" in tokens:
        tokens.remove("")

    return tokens
