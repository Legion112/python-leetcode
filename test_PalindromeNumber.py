import pytest

from PalindromeNumber import Solution


@pytest.mark.parametrize("number,expected", [
    (121, True),  # Example 1
    (123, False),  # Example 1
])
def test_solution(number: int, expected: bool):
    solution = Solution()

    assert solution.isPalindrome(number) == expected
