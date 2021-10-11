"""
You are given an array of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

    For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".

A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given list of words.
"""
# bottom 5% execution time :'(
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))
        hops_map = {}
        hops_map_2 = {}
        hops_map_max = {}

        def is_off_by_one(word1, word2):
            assert len(word1) < len(word2)
            diffs = 0
            for idx, char in enumerate(word2):
                if word == word2[:idx] + word2[idx+1:]:
                    return True
            return False

        def get_depth(word):
            if word in hops_map_max:
                return hops_map_max[word]
            if word not in hops_map_2:
                hops_map_max[word] = 1
                return 1
            depth = max(get_depth(word2) for word2 in hops_map_2[word])
            hops_map_max[word] = depth + 1
            return depth + 1

        for word in words:
            hops_map[word] = []
            for word2 in words:
                if len(word2) == len(word) + 1:
                    hops_map[word].append(word2)

        for word, next_words in hops_map.items():
            for word2 in next_words:
                if not is_off_by_one(word, word2):
                    continue
                if word2 in hops_map_2:
                    hops_map_2[word2].append(word)
                else:
                    hops_map_2[word2] = [word]

        max_depth = 0
        for word in words:
            depth = get_depth(word)
            if depth > max_depth:
                max_depth = depth
        return max_depth
