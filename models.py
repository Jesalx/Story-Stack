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
    A class representing a database model for a user account.

    Attributes:
        id (int): The database id of the user.
        email (str): The email of the user.
        username (str): The unique username of the user.
        password (str): The hashed password of the user.
        bio (str): A short description of the user.
    """

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    password = db.Column(db.String(256), unique=False, nullable=True)
    bio = db.Column(db.String(256), unique=False, nullable=True)

    def __repr__(self):
        return f"User {self.username}"


class Comment(db.Model):
    """
    A class representing a database model for comments on posts.

    Attributes:
        id (int): The database id of the comment.
        userid (int): The database id of the user who posted the comment.
        storyid (int): The database id of the story the comment is on.
        text (str): The text of the comment.
    """

    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, unique=False, nullable=False)
    storyid = db.Column(db.Integer, unique=False, nullable=False)
    text = db.Column(db.String(128), unique=False, nullable=False)

    def __repr__(self):
        return f"Comment {self.text}"


class Like(db.Model):
    """
    A class that represent a database model for likes on a post.

    Attributes:
        id (int): The database id of the like.
        userid (int): The database id of the user who liked the post.
        storyid (int): The database id of the story the like is on.
    """

    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, unique=False, nullable=False)
    storyid = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return f"Like {self.userid} {self.storyid}"


tag_story_helper = db.Table(
    "tag_story_helper",
    db.Column("id", db.Integer, primary_key=True),
    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id")),
    db.Column("story_id", db.Integer, db.ForeignKey("story.id")),
)


class Tag(db.Model):
    """
    A class that represents a database model for a tag associated with
    a story. The user creates the tags when creating a story. Tags are
    meant to be used for exploring categories of stories that interest
    a user.

    Attributes:
        id (int): The database id of the tag.
        name (str): The name of the tag.
        stories (list): A list of stories associated with the tag.
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1028), unique=False, nullable=False)
    stories = db.relationship(
        "Story", secondary=tag_story_helper, back_populates="tags"
    )

    def __repr__(self):
        return f"Tag {self.name}"


class Story(db.Model):
    """
    A class that represents a database model for a story.

    Attributes:
        id (int): The database id of the story.
        parent (int): The database id of the parent story. This will contain
        -1 if the story is a top level story.
        userid (int): The database id of the user who created the story.
        title (str): The title of the story.
        text (str): The text of the story.
        tags (list): A list of tags associated with the story.
        date_posted (datetime): The date the story was posted.
        date_updated (datetime): The date the story was most recently updated.
    """

    id = db.Column(db.Integer, primary_key=True)
    parent = db.Column(db.Integer, unique=False, nullable=True)
    userid = db.Column(db.Integer, unique=False, nullable=True)
    title = db.Column(db.String(32), unique=False, nullable=True)
    text = db.Column(db.String(2048), unique=False, nullable=False)
    tags = db.relationship("Tag", secondary=tag_story_helper, back_populates="stories")
    date_posted = db.Column(db.Date, default=get_date, unique=False, nullable=False)
    date_updated = db.Column(db.Date, onupdate=get_date, unique=False, nullable=True)

    def __repr__(self):
        return f"Story {self.text}"
