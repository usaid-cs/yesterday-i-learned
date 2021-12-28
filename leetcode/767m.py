"""
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.
"""
# This is a greedy approach taking the most frequent letter that isn't the last one used
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        # Build a counter of character counts
        c = Counter()
        for char in s:
            c[char] += 1

        buffer = ''
        while any(x for x in c.values() if x > 0):
            frequencies = c.most_common()
            char = ''
            # Take the most popular character that is not the one we just used
            for k, v in frequencies:
                if v <= 0:
                    continue
                if buffer and k == buffer[-1]:
                    continue
                char = k
                break
            if not char:
                # There is no way this string will be rebuilt with remaining characters.
                return ''
            buffer += char
            c[char] -= 1
        if len(buffer) != len(s):
            return ''
        return buffer
