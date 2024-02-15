import pytest
from FindTheIndexOfTheFirstOccurrenceInAString import Solution


@pytest.mark.parametrize("haystack,needle,expected", [
    ("sadbutsad", "sad", 0),
    ("leetcode", "leeto", -1),
    ("aaa", "aaaa", -1),
])
def test_str_str(haystack: str, needle: str, expected: int) -> None:
    assert expected == Solution().strStr(haystack, needle)
