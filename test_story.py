"""
Module for testing story.py
"""
# pylint: disable=missing-function-docstring
import unittest
from story import extract_tags


class ExtractTagsTests(unittest.TestCase):
    """
    This Class contains test for the extract_tags function of story.py
    """

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


if __name__ == "__main__":
    unittest.main()
