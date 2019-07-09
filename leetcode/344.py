from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if not s:
            return
        l = len(s)
        if l % 2 == 0:  # even
            for i in range(l // 2):
                s[i], s[l - i - 1] = s[l - i - 1], s[i]
        else:
            print('odd string')
            for i in range((l - 1) // 2):
                s[i], s[l - i - 1] = s[l - i - 1], s[i]


a = Solution()
s = ["h", "e", "l", "l", "o"]
a.reverseString(s)
assert s == ["o", "l", "l", "e", "h"], s

s = ["H", "a", "n", "n", "a", "h"]
a.reverseString(s)
assert s == ["h", "a", "n", "n", "a", "H"], s
