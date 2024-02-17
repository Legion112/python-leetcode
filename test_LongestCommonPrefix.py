import pytest
from typing import List
from LongestCommonPrefix import Solution

@pytest.mark.parametrize("data,expected", [
    (["flower", "flow", "flight"], "fl"),
    (["dog", "racecar", "car"], ""),
    (["abc", "abcd", "abcde"], "abc"),
    (["aa", "a"], "a"),
    ([], ""),
    ([""], ""),
])
def test_solution(data: List[str], expected: str):
    assert Solution().longestCommonPrefix(data) == expected