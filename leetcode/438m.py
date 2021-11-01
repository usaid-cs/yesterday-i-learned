"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        string = s
        part = p
        if len(part) > len(string):
            return []  # can't possibly be it

        def get_hash(s):
            has = {}
            for char in s:
                if char in has:
                    has[char] += 1
                else:
                    has[char] = 1
            return has

        ans = []
        target_length = len(part)
        string_hash = {}
        part_hash = get_hash(part)
        for idx, char in enumerate(string):
            if char not in string_hash:
                string_hash[char] = 0
            string_hash[char] += 1
            if idx >= len(part):
                string_hash[string[idx - target_length]] -= 1
            if {k: v for k, v in string_hash.items() if v} == part_hash:
                ans.append(idx - target_length + 1)

        return ans