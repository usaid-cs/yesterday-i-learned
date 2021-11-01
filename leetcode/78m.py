"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        for num in nums:
            # Add an item to it every time.
            # e.g. if nums is [1,2,3]
            # [[]                                               ]
            # [[],                [1]                           ]
            # [[],      [2],      [1],         [1, 2]           ]
            # [[], [3], [2], [3], [1], [1, 3], [1, 2], [1, 2, 3]]
            output += [curr + [num] for curr in output]

        return output