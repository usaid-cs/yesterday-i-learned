"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0

        for idx, num in enumerate(nums):
            if idx <= farthest and idx + num > farthest:
                farthest = idx + num

        return farthest >= len(nums) - 1