import pytest
from TwoSum import Solution

@pytest.mark.parametrize("nums,target,expected", [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 3], 6, [0, 1]),
])
def test_two_sum(nums, target, expected):
    solution = Solution()
    result = solution.twoSum(nums, target)
    assert result == expected, f"Failed for nums: {nums} with target: {target}. Expected: {expected}, got: {result}"

def test_two_sum_no_return_value():
    solution = Solution()
    result = solution.twoSum([3, 3], 0)
    assert result is None, f"Expected: None, got: {result}"
