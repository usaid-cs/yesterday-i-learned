"""
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(log n) time.
"""
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        new_start = 0
        searches = [(1, len(nums) - 1)]
        while searches:
            left, right = searches.pop(0)
            if left > right:
                continue
            middle = (left + right) // 2
            has_lesser_left = (
                (middle == 0) or
                nums[middle] > nums[middle - 1]
            )
            has_lesser_right = (
                (middle == len(nums) - 1) or
                nums[middle] > nums[middle + 1]
            )
            if has_lesser_left and has_lesser_right:
                return middle
            else:
                searches.append((left, middle - 1))
                searches.append((middle + 1, right))
        return 0
