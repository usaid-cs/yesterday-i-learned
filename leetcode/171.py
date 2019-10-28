class Solution:
    def titleToNumber(self, s: str) -> int:
        total = 0
        exp = 0
        while s:
            last_char = s[-1]
            val = ord(last_char) - 64  # So A = 1
            total += val * 26**exp
            s = s[:-1]
            exp += 1
        return total


a = Solution()
assert a.titleToNumber("A") == 1
assert a.titleToNumber("Z") == 26
assert a.titleToNumber("AA") == 27
assert a.titleToNumber("AB") == 28
assert a.titleToNumber("ZY") == 701, a.titleToNumber("ZY")