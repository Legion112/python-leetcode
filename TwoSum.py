from typing import List, Optional, Dict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> Optional[List[int]]:
        hashmap: Dict[int:int] = {value: key for key, value in enumerate(nums)}
        for firstIndex, firstValue in enumerate(nums):
            second_index: Optional[int] = hashmap.get(target - firstValue)
            if second_index is not None and second_index != firstIndex:
                return [firstIndex, second_index]
        print("No value to return")
        return None
