class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        original_charset = "abcdefghijklmnopqrstuvwxyz"

        def subl(word):
            buffer = ""
            for char in word:
                idx = order.index(char)
                buffer += original_charset[idx]
            return buffer

        actual_words = [subl(word) for word in words]
        return list(sorted(actual_words)) == actual_words
