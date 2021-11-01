"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

    [4,5,6,7,0,1,2] if it was rotated 4 times.
    [0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
"""
# This is basically 33m but easier
class Solution:
    def findMin(self, nums: List[int]) -> int:
        new_start = 0
        searches = [(0, len(nums) - 1)]
        while searches:
            left, right = searches.pop(0)
            if left > right:
                continue
            middle = (left + right) // 2
            if middle > 0 and nums[middle - 1] > nums[middle]:
                return nums[middle]
            else:
                searches.append((left, middle - 1))
                searches.append((middle + 1, right))
        return nums[0]
