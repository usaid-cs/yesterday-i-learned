"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        moneys = [0 for _ in nums]
        moneys[0] = nums[0]
        if len(nums) == 1:
            return moneys[-1]

        moneys[1] = max(nums[0], nums[1])
        if len(nums) == 2:
            return moneys[-1]

        for idx, num in enumerate(nums):
            if idx < 2:
                continue
            moneys[idx] = max(
                moneys[idx - 2] + num,
                moneys[idx - 1]
            )
        return moneys[-1]