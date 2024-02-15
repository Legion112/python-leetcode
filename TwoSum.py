from typing import List, Optional, Dict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> Optional[List[int]]:
        hashmap: Dict[int, int] = {
            value: key for key, value in enumerate(nums)}
        for firstIndex, firstValue in enumerate(nums):
            secondIndex: Optional[int] = hashmap.get(target - firstValue)
            if secondIndex is not None and secondIndex != firstIndex:
                return [firstIndex, secondIndex]
        return None
