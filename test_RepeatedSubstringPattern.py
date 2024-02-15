import pytest

from RepeatedSubstringPattern import Solution


@pytest.mark.parametrize("s,expected", [
    ("abab", True),  # "ab"
    ("aba", False),  # Example 1
    ("abcabcabcabc", True),  # "abc" four times
])
def test_repeated_substring_pattern(s: str, expected: bool):
    assert expected == Solution().repeatedSubstringPattern(s)
