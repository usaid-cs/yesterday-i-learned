"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Backtracking solution
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        n = len(nums)

        def recurse(first):
            if first == n:
                results.append(nums[:])  # copy of nums at the current state
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]  # swap the numbers here
                recurse(first + 1)
                nums[first], nums[i] = nums[i], nums[first]  # swap the numbers back (backtrack)

        recurse(0)
        return results
