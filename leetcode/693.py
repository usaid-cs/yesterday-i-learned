class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        digits = bin(n)[2:]
        for digit1, digit2 in zip(digits[:-1], digits[1:]):
            if digit1 == digit2:
                return False
        return True


a = Solution()
assert a.hasAlternatingBits(1) == True
assert a.hasAlternatingBits(5) == True
assert a.hasAlternatingBits(7) == False
assert a.hasAlternatingBits(11) == False
assert a.hasAlternatingBits(10) == True