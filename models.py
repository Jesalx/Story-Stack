"""
This module contains the models used in the database for
the application
"""
# pylint: disable=no-member
# pylint: disable=too-few-public-methods
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class Account(db.Model, UserMixin):
    """
    A class that represents a single user account.
    Contains username and hashed password.
    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(512))
