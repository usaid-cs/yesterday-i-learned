class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars_s = [_ for _ in s]
        chars_s.sort()
        chars_t = [_ for _ in t]
        chars_t.sort()
        return chars_s == chars_t