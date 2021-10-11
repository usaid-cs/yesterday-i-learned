"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

    Insert a character
    Delete a character
    Replace a character

"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        d = []
        for _ in range(len(word1) + 1):
            a = [0] * (len(word2) + 1)
            d.append(a)

        # word1 goes down
        # word2 goes left

        for i in range(len(word2) + 1):
            d[0][i] = i

        for i in range(len(word1) + 1):
            d[i][0] = i

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    d[i][j] = d[i - 1][j - 1]
                else:
                    d[i][j] = min(
                        d[i - 1][j - 1],  # replacing a letter
                        d[i][j - 1],  # inserting a letter
                        d[i - 1][j]  # deleting a letter
                    ) + 1  # cost is always 1
        return d[-1][-1]
