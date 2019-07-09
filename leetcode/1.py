from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = 0
        while True:
            other_nums = nums[idx + 1:]
            for other_idx, other_num in enumerate(other_nums):
                if nums[idx] + other_num == target:
                    return [idx, idx + other_idx + 1]
            idx += 1