# pylint: disable=no-member
# pylint: disable=too-few-public-methods
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
import datetime

db = SQLAlchemy()


def get_date():
    return datetime.datetime.now()


class Account(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    # this has been left nullable to allow for users logging in using google oauth not to have to also set a password. login attempts or account creation attempts without a password should still not be allowed
    password = db.Column(db.String(256), unique=False, nullable=True)
    # no particular reason for the bio being 256 chars maximum, consider placeholder length
    bio = db.Column(db.String(256), unique=False, nullable=True)
    email = db.Column(db.String(128), unique=True, nullable=True)

    def __repr__(self):
        return "User %r" % self.username


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, unique=False, nullable=False)
    storyid = db.Column(db.Integer, unique=False, nullable=False)
    text = db.Column(db.String(128), unique=False, nullable=False)

    def __repr__(self):
        return "Comment %r" % self.text


class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, unique=False, nullable=False)
    storyid = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return "Like %r %r" % self.userid % self.storyid


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, unique=False, nullable=False)
    storyid = db.Column(db.Integer, unique=False, nullable=False)
    text = db.Column(db.String(128), unique=False, nullable=False)

    def __repr__(self):
        return "Tag %r" % self.text


class Story(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    parent = db.Column(db.Integer, unique=False, nullable=True)
    userid = db.Column(db.Integer, unique=False, nullable=True)
    text = db.Column(db.String(128), unique=False, nullable=False)
    date_posted = db.Column(db.Date, default=get_date, unique=False, nullable=False)
    date_updated = db.Column(db.Date, onupdate=get_date, unique=False, nullable=True)
    title = db.Column(db.String(32), unique=False, nullable=True)

    def __repr__(self):
        return "User %r" % self.text
