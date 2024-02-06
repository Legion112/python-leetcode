import unittest

from TwoSum import Solution


class TestSolution(unittest.TestCase):
    def test_two_sum(self):
        test_cases = [
            ([2, 7, 11, 15], 9, [0, 1]),
            ([3, 2, 4], 6, [1, 2]),
            ([3, 3], 6, [0, 1]),
        ]
        solution = Solution()
        for nums, target, expected in test_cases:
            with self.subTest(nums=nums, target=target, expected=expected):
                result = solution.twoSum(nums, target)
                self.assertListEqual(result, expected,
                                     f"Failed for nums: {nums} with target: {target}. Expected: {expected}, got: {result}")

    def test_two_sum_no_return_value(self):
        solution = Solution()
        result = solution.twoSum([3, 3], 0)
        self.assertIsNone(result, f"Expected: None, got: {result}")
