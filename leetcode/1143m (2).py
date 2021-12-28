"""
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

    For example, "ace" is a subsequence of "abcde".

A common subsequence of two strings is a subsequence that is common to both strings.
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1 = len(text1)
        len2 = len(text2)

        dp = [[0] * (len2 + 1) for _ in text1 + "x"]

        for idx1 in range(1, len1 + 1):
            for idx2 in range(1, len2 + 1):
                if text1[idx1 - 1] == text2[idx2 - 1]:
                    dp[idx1][idx2] = dp[idx1 - 1][idx2 - 1] + 1
                else:
                    dp[idx1][idx2] = max(dp[idx1 - 1][idx2],
                                         dp[idx1][idx2 - 1])
        return dp[-1][-1]