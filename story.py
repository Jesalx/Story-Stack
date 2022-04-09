"""
File containing backend functions for the processing of stories.
"""
from models import db, Account
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
