"""
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.
"""
# (I cheated because it's next to impossible to figure that out but here are some notes)
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0  # It is impossible to have any product of any number multiply up to less than 0 when the numbers start from 1
        left = 0
        answers = 0

        current = 1
        for right, num in enumerate(nums):
            current *= num
            while current >= k:
                current /= nums[left]
                left += 1
            # "the number of intervals with subarray product less than k and with right-most coordinate right, is right - left + 1"
            # e.g. [5, 2, 6]
            # [5] (0 - 0) + 1 = 1          # 5
            # [5, 2] (1 - 0) + 1 = 2       # 2, 5 * 2
            # [5, 2, 6] (2 - 0) + 1 = 3    # 6, 2 * 6, 5 * 2 * 6
            answers += right - left + 1
        return answers