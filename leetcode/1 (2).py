from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            raise RuntimeError
        for idx, num in enumerate(nums):
            try:
                complement_index = nums.index(target - num)
            except ValueError:  # "Not in the list"
                pass
            if idx != complement_index:
                return [idx, complement_index]
