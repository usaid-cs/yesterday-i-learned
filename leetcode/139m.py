from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = sorted(wordDict, key=len, reverse=True)
        shortest_word = wordDict[-1]
        def recurse(string):
            if len(string) == len(shortest_word):
                for word in wordDict:
                    if string == word:
                        return True
                return False
            for word in wordDict:
                if string == word:
                    return True
                if string.startswith(word):
                    new_string = string[len(word):]
                    if recurse(new_string):
                        return True
            return False

        return recurse(s)

a = Solution()
a.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
            ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])
