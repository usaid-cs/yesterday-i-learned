class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        for i in range(100000000000):
            i3 = 3**i
            if i3 == n:
                return True
            if i3 > n:
                return False
        return False


a = Solution()
assert a.isPowerOfThree(27) == True
assert a.isPowerOfThree(0) == False
assert a.isPowerOfThree(9) == True
assert a.isPowerOfThree(45) == False
assert a.isPowerOfThree(1) == True
