"""
Module containing backend functions for the processing of stories.
"""
# pylint: disable=no-member
from models import db, Account, Tag, Story
from werkzeug.security import generate_password_hash
import re


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


def add_tags(story, tags):
    """
    Takes a story and a list of tags and then adds a relationship between
    the two in their respective models.
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
    """
    original_poster = Account.query.filter_by(id=story.userid).first()
    if original_poster:
        return original_poster.username
    return "Anonymous"


def get_displayable_stories(stories: list) -> list:
    """
    Take a list of stories from the Story model and returns a list of those
    story objects, but represented in dict form so that they are easier to
    display with Jinja templates.
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


def add_user(user):
    if not (user.email and user.username and user.password):
        return False
    db.session.add(user)
    db.session.commit()
    return True


def post_story(story):
    if not (story.parent and story.title and story.text and story.userid):
        return False
    db.session.add(story)
    db.session.commit()
    return True


def parse_id(id_str: str) -> int:
    """
    Takes a string and returns the integer in s, or 0 if s is not an integer
    or below 0.
    """
    try:
        return max(int(id_str), 0)
    except ValueError:
        return 0
