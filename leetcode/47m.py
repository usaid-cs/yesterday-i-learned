"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
"""
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        ans = []

        def recurse(first=0):
            if first == len(nums):
                ayy = tuple(nums)
                if ayy not in ans:
                    ans.append(ayy)
            for i in range(first, len(nums)):
                nums[i], nums[first] = nums[first], nums[i]
                recurse(first + 1)
                nums[i], nums[first] = nums[first], nums[i]

        recurse()
        return [list(x) for x in ans]