"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""
# Holy balls even an O(n) solution is slower than average
from functools import lru_cache

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i in range(len(nums)):
            # "It will only add the jump length to declare a new farthest
            # if you are already on a square you know you can jump to
            # (i.e. it is less than or equal to the previous farthest value)."
            # - SimonChen2002
            if i <= farthest:
                farthest = max(farthest, nums[i] + i)
        return farthest >= len(nums) - 1