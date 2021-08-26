class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = {}
        for char in s:
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
        unique_chars = [x for (x, count_) in chars.items() if count_ == 1]
        unique_chars.sort(key=lambda x: s.index(x))
        if unique_chars:
            return s.index(unique_chars[0])
        return -1
