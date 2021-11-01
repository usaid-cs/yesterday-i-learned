"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = [0 for _ in nums]
        ans[0] = nums[0]

        for idx, num in enumerate(nums):
            if idx > 0:
                ans[idx] = max(num, num + ans[idx - 1])

        return max(ans)