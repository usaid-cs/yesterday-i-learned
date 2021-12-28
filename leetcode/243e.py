"""
Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.
"""
class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        poss1 = [idx for idx, word in enumerate(wordsDict) if word == word1]
        poss2 = [idx for idx, word in enumerate(wordsDict) if word == word2]

        min_distance = float('inf')
        for pos1 in poss1:
            for pos2 in poss2:
                min_distance = min(min_distance, abs(pos1 - pos2))
        return min_distance