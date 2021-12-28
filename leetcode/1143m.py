# See also: 516m
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1 = len(text1)
        len2 = len(text2)
        computed = []
        for _ in range(len1 + 1):
            col = [0] * (len2 + 1)
            computed.append(col)

        for i in range(1, len1 + 1):
            char = text1[i - 1]
            for j in range(1, len2 + 1):
                char2 = text2[j - 1]
                if char == char2:
                    computed[i][j] = computed[i - 1][j - 1] + 1
                else:
                    computed[i][j] = max(computed[i - 1][j], computed[i][j - 1])
        return computed[i][j]
