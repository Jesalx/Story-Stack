"""
This module contains the models used in the database for
the application
"""
# pylint: disable=no-member
# pylint: disable=too-few-public-methods
import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


def get_date():
    """
    Returns the current date
    """
    return datetime.datetime.now()


class Account(db.Model, UserMixin):
    """
    A Class that represents a single user account containing
    username, password, and email.
    TODO - Implement bio
    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    # this has been left nullable to allow for users logging in using
    # google oauth not to have to also set a password. login attempts or
    # account creation attempts without a password should still not be allowed
    password = db.Column(db.String(256), unique=False, nullable=True)
    bio = db.Column(db.String(256), unique=False, nullable=True)
    email = db.Column(db.String(128), unique=True, nullable=True)

    def __repr__(self):
        return f"User {self.username}"


class Comment(db.Model):
    """
    A Class that represents a single comment on a Post. It contains
    the comment text, the user_id of poster, and the post_id
    """

    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, unique=False, nullable=False)
    storyid = db.Column(db.Integer, unique=False, nullable=False)
    text = db.Column(db.String(128), unique=False, nullable=False)

    def __repr__(self):
        return f"Comment {self.text}"


class Like(db.Model):
    """
    A Class that represents a single like on a Post. It contains
    the post and the user who liked it.
    TODO - Implement likes
    """

    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, unique=False, nullable=False)
    storyid = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return f"Like {self.userid} {self.storyid}"


class Tag(db.Model):
    """
    A Class containign the tags for a post. The user creates the tags
    when creating a story. Tags are meant to be used for exploring
    categories of stories that interest a user.
    """

    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, unique=False, nullable=False)
    storyid = db.Column(db.Integer, unique=False, nullable=False)
    text = db.Column(db.String(128), unique=False, nullable=False)

    def __repr__(self):
        return f"Tag {self.text}"


class Story(db.Model):
    """
    A Class that represents a single story. It contains the story text,
    the user_id of poster, a title, and time of posting/editing.
    """

    id = db.Column(db.Integer, primary_key=True)
    parent = db.Column(db.Integer, unique=False, nullable=True)
    userid = db.Column(db.Integer, unique=False, nullable=True)
    text = db.Column(db.String(128), unique=False, nullable=False)
    date_posted = db.Column(db.Date, default=get_date, unique=False, nullable=False)
    date_updated = db.Column(db.Date, onupdate=get_date, unique=False, nullable=True)
    title = db.Column(db.String(32), unique=False, nullable=True)

    def __repr__(self):
        return f"User {self.text}"
