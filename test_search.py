"""
Module for testing search.py
"""
# pylint: disable=missing-function-docstring

import unittest
from search import get_query_tokens


class GetQueryTokensTests(unittest.TestCase):
    """
    This Class contains tests for the get_query_tokens function of search.py
    """

    def test_regular_string(self):
        test_string = "Sci-Fi Fantasy Adventure"
        expected_output = set(["sci-fi", "fantasy", "adventure"])
        actual_output = get_query_tokens(test_string)
        self.assertEqual(expected_output, actual_output)

    def test_duplicate_string(self):
        test_string = "word1 word1 word1"
        expected_output = set(["word1"])
        actual_output = get_query_tokens(test_string)
        self.assertEqual(expected_output, actual_output)

    def test_empty_string(self):
        test_string = ""
        expected_output = set([])
        actual_output = get_query_tokens(test_string)
        self.assertEqual(expected_output, actual_output)

    def test_whitespace_string(self):
        test_string = "     "
        expected_output = set([])
        actual_output = get_query_tokens(test_string)
        self.assertEqual(expected_output, actual_output)

    def test_short_string(self):
        test_string = "word"
        expected_output = set(["word"])
        actual_output = get_query_tokens(test_string)
        self.assertEqual(expected_output, actual_output)

    def test_weird_string(self):
        test_string = ",,,,,,,word1,,,, ,,,,,@@@@,,,,,,word2"
        expected_output = set([",,,,,,,word1,,,,", ",,,,,@@@@,,,,,,word2"])
        actual_output = get_query_tokens(test_string)
        self.assertEqual(expected_output, actual_output)

    def test_extra_whitespace_string(self):
        test_string = "word1   word2          word3"
        expected_output = set(["word1", "word2", "word3"])
        actual_output = get_query_tokens(test_string)
        self.assertEqual(expected_output, actual_output)


if __name__ == "__main__":
    unittest.main()
