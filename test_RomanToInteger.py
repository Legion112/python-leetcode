import pytest
from RomanToInteger import Solution


@pytest.mark.parametrize("roman_string,output", [
    ("III", 3),  # Example 1
    ("LVIII", 58),  # Example 2
    ("MCMXCIV", 1994),  # Example 3
])
def test_roman_to_int(roman_string, output):
    assert Solution().romanToInt(roman_string) == output
