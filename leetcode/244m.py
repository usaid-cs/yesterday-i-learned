# Times out
class WordDistance:
    wordsDict = None
    posss = None

    def __init__(self, wordsDict: List[str]):
        self.wordsDict = wordsDict
        self.posss = {}
        for word1 in wordsDict:
            self.posss[word1] = [idx for idx, word in enumerate(self.wordsDict) if word == word1]

    def shortest(self, word1: str, word2: str) -> int:
        poss1 = self.posss[word1]
        poss2 = self.posss[word2]

        min_distance = float('inf')
        for pos1 in poss1:
            for pos2 in poss2:
                min_distance = min(min_distance, abs(pos1 - pos2))
        return min_distance


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)