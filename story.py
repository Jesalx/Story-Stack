"""
Module containing backend functions for the processing of stories.
"""
# pylint: disable=no-member
from models import db, Account, Tag, Story


def extract_tags(input_string: str) -> set:
    """
    Takes a "," separated string of words and returns a set of those cleaned
    words.

    NOTE: This function is not currently used. It has been replaced
    by the get_query_tokens function in search.py. Once we finalize
    if we want to go with the new search system, we can remove this.

    Args:
        input_string (str): A string representing a list of keywords/genres.

    Returns:
        set: A set of strings containing keywords/genres.
    """
    tags = set()
    for tag in input_string.split(","):
        cleaned_tag = tag.strip().lower()
        tags.add(cleaned_tag)

    if "" in tags:
        tags.remove("")

    return tags


def add_tags(story: Story, tags: set):
    """
    Takes a story and a set of tags and then adds a relationship between
    the two in their respective models.

    Args:
        story (Story): A single story object to add tag relationships to.
        tags (set): A set of tags to be added to the story.
    """
    for tag in tags:
        tag_obj = Tag.query.filter_by(name=tag).first()
        if not tag_obj:
            tag_obj = Tag(name=tag)
            db.session.add(tag_obj)
            db.session.commit()
    db.session.commit()

    for tag in tags:
        tag_obj = Tag.query.filter_by(name=tag).first()
        story.tags.append(tag_obj)
    db.session.commit()


def get_poster_username(story: Story) -> str:
    """
    Takes a story and returns a string of the username of the user who
    wrote the story unless the story is orphaned, in which case it returns
    'Anonymous'.

    Args:
        story (Story): A story object to retrieve the username of the poster.

    Returns:
        str: A string containing the username of the poster or 'Anonymous'.
    """
    original_poster = Account.query.filter_by(id=story.userid).first()
    return original_poster.username if original_poster else "Anonymous"


def get_displayable_stories(stories: list) -> list:
    """
    Takes a list of stories from the Story model and returns a list of those
    story objects, but represented in a dictionary so that they are easier
    to display with Jinja templates.

    Args:
        stories (list): A list of story objects.

    Returns:
        list: A list of dictionaries containing story information.
    """
    results = []
    for story_obj in stories:
        story_dict = {}
        story_dict["id"] = story_obj.id
        story_dict["poster"] = get_poster_username(story_obj)
        story_dict["title"] = story_obj.title
        story_dict["text"] = story_obj.text
        story_dict["creation_date"] = story_obj.date_posted
        results.append(story_dict)
    return results


def add_user(user: Account) -> bool:
    """
    Adds a user to the database if the User object contains valid
    fields.

    NOTE: This function is not currently in use.

    Args:
        user (Account): An Account object to add to the database.

    Returns:
        bool: A boolean representing if the user was added to the database.
    """
    if not (user.email and user.username and user.password):
        return False
    db.session.add(user)
    db.session.commit()
    return True


def post_story(story: Story) -> bool:
    """
    Adds a story to the database if the Story object contains valid fields.

    Args:
        story (Story): A Story object to add to the database.

    Returns:
        bool: A boolean representing if the story was added to the database.
    """
    if not (story.parent and story.title and story.text and story.userid):
        return False
    db.session.add(story)
    db.session.commit()
    return True


def parse_id(id_str: str) -> int:
    """
    Takes a string and returns the integer in s, or 0 if s is not a valid
    integer. A valid integer is an integer greater than 0.

    Args:
        id_str (str): A string containing an integer.

    Returns:
        int: An integer representing the integer in s, or if s is not a valid
        integer, 0.
    """
    try:
        return max(int(id_str), 0)
    except ValueError:
        return 0
