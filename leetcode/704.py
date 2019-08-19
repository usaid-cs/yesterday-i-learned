from typing import List
import math


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            idx = (left + right) // 2  # middle
            num = nums[idx]
            print(left, right, idx, num)
            if num == target:
                return idx
            if left == right:
                return -1  # not found
            if num < target:
                # Cut the search space in half (just the right hand side)
                left = idx + 1
            else:
                right = idx - 1
        return -1


a = Solution()
assert a.search([-1, 0, 3, 5, 9, 12], 9) == 4
assert a.search([-1, 0, 3, 5, 9, 12], 2) == -1
