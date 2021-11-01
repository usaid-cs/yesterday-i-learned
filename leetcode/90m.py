"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        for num in nums:
            # Add an item to it every time.
            # e.g. if nums is [1,2,3]
            # [[]                                               ]
            # [[],                [1]                           ]
            # [[],      [2],      [1],         [1, 2]           ]
            # [[], [3], [2], [3], [1], [1, 3], [1, 2], [1, 2, 3]]
            output += [curr + [num] for curr in output]

        # I mean, I don't think I learned much from this vs say 78m
        output = [sorted(x) for x in output]
        output = [tuple(x) for x in output]
        output = list(set(output))
        output.sort()
        output = [list(x) for x in output]

        return output