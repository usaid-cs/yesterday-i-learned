class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s2 = ''.join([t for t in s if t.isalnum()])

        return s2 == s2[::-1]
