"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for idx in range(len(nums)):
            if nums[idx] != idx:
                return idx
        return len(nums)