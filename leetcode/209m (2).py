"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.
"""
# you probably won't get any faster than this
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        answer = None

        current = 0
        for right, num in enumerate(nums):
            current += num
            while current >= target:
                if answer is None:
                    # wait, why is it right - left + 1, not just right - left?
                    answer = right - left + 1
                else:
                    answer = min(answer, right - left + 1)
                current -= nums[left]
                left += 1
        return answer or 0