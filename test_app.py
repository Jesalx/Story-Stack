import unittest
from venv import create

import flask
from mock_alchemy.mocking import AlchemyMagicMock
from story import post_story, add_user
from models import db, Account, Story
from werkzeug.security import generate_password_hash


class PostDatabaseTests(unittest.TestCase):
    def test_valid_post(self):
        new_story = Story(
            parent=-1,
            userid=1,
            text="hello",
            title="good title",
        )
        db.session = AlchemyMagicMock()
        test = post_story(new_story)
        self.assertTrue(test)

    def test_null_post(self):
        new_story = Story(parent=None, userid=None, text=None, title=None)
        db.session = AlchemyMagicMock()
        test = post_story(new_story)
        self.assertFalse(test)


class AccountDatabaseTests(unittest.TestCase):
    def test_valid_user(self):
        new_user = Account(
            email="your@email.com",
            username="username",
            password=generate_password_hash("password", method="sha256"),
        )
        db.session = AlchemyMagicMock()
        test = add_user(new_user)
        self.assertTrue(test)

    def test_null_user(self):
        new_user = Account(email=None, username=None, password=None)
        db.session = AlchemyMagicMock()
        test = add_user(new_user)
        self.assertFalse(test)


if __name__ == "__main__":
    unittest.main()
