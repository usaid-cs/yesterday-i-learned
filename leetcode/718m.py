"""
Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

This is the exact same question as the longest common substring question.
"""
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        A = nums1
        B = nums2
        memo = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                if A[i - 1] == B[j - 1]:
                    memo[i][j] = memo[i - 1][j - 1] + 1
        return max(max(row) for row in memo)