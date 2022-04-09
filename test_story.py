import unittest
from story import extract_tags
from werkzeug.security import generate_password_hash
from app import create_user
from models import Account


class ExtractTagsTests(unittest.TestCase):
    def test_regular_string(self):
        test_string = "tag1, tag2, tag3"
        expected_output = set(["tag1", "tag2", "tag3"])
        actual_output = extract_tags(test_string)
        self.assertEqual(expected_output, actual_output)

    def test_empty_string(self):
        test_string = ""
        expected_output = set([])
        actual_output = extract_tags(test_string)
        self.assertEqual(expected_output, actual_output)

    def test_whitespace_string(self):
        test_string = "     "
        expected_output = set([])
        actual_output = extract_tags(test_string)
        self.assertEqual(expected_output, actual_output)

    def test_short_string(self):
        test_string = "tag1"
        expected_output = set(["tag1"])
        actual_output = extract_tags(test_string)
        self.assertEqual(expected_output, actual_output)

    def test_weird_string(self):
        test_string = ",,,,,,,tag1,,,,,,,,,@@@@,,,,,,tag2"
        expected_output = set(["tag1", "tag2", "@@@@"])
        actual_output = extract_tags(test_string)
        self.assertEqual(expected_output, actual_output)

    def test_comma_string(self):
        test_string = ",,,,,,,,,,,,,"
        expected_output = set([])
        actual_output = extract_tags(test_string)
        self.assertEqual(expected_output, actual_output)

    def test_nospace_regular_string(self):
        test_string = "tag1,tag2,tag3"
        expected_output = set(["tag1", "tag2", "tag3"])
        actual_output = extract_tags(test_string)
        self.assertEqual(expected_output, actual_output)


class CreateUserTests(unittest.TestCase):
    def test_valid_submission(self):
        exp_user = Account(
            email="alex2012smith@gmail.com",
            username="alex2012",
            password=generate_password_hash("smith0122", method="sha256"),
        )
        actual_user = create_user("alex2012smith@gmail.com", "alex2012", "smith0122")
        self.assertEqual(exp_user, actual_user)

    def test_empty_submission(self):
        user = create_user(None, None, None)
        self.assertFalse(user)

    def test_bad_email(self):
        user = create_user("spinach@@@", "saltine", "cracker")
        self.assertFalse(user)


if __name__ == "__main__":
    unittest.main()
