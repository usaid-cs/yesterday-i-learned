"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

You aren't supposed to do it this way. See another file for backtracking
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []

        def recurse(lst, rest):
            if not rest:
                results.append(lst)
                return
            for idx, num in enumerate(rest):
                # print(rest)
                rest_lst = rest[:idx] + rest[idx + 1:]
                # print(rest_lst)
                recurse(lst + [num], rest_lst)

        recurse([], nums)
        return results
