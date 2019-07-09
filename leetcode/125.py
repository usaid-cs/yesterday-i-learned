class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        s = [x.lower() for x in s if x.isalpha() or x.isnumeric()]
        rs = list(reversed(s))
        return s == rs


a = Solution()
assert a.isPalindrome('alla')