"""
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
"""
# Note that this is just a spin off 1143m, where the second string is the reverse of the input
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        len_s = len(s)
        computed = []
        for _ in range(len_s + 1):
            computed.append(["" for _ in range(len_s + 1)])

        t = s[::-1]  # reverse

        for i in range(1, len_s + 1):
            for j in range(1, len_s + 1):
                char1 = s[i - 1]
                char2 = t[j - 1]
                if char1 == char2:
                    computed[i][j] = computed[i - 1][j - 1] + char1
                else:
                    candidate1 = computed[i - 1][j]
                    candidate2 = computed[i][j - 1]
                    if len(candidate1) < len(candidate2):
                        computed[i][j] = candidate2
                    else:
                        computed[i][j] = candidate1
        return len(computed[i][j])
