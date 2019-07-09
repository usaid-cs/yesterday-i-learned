class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        chars = {}
        for char in s:
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1

        singles = [k for k, v in chars.items() if v == 1]
        if not singles:
            return -1
        for idx, char in enumerate(s):
            if char in singles:
                return idx