from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_chars = defaultdict(int)
        for char in magazine:
            mag_chars[char] += 1
        for char in ransomNote:
            mag_chars[char] -= 1
        print(mag_chars)
        return not any(x for x in mag_chars.values() if x < 0)