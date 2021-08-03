class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 1:
            return True
        if n <= 0:
            return False

        candidates = [2,3,5]

        def recurse(cur):
            if cur in candidates:
                return True
            for candidate in candidates:
                if cur / candidate == cur // candidate:
                    if recurse(cur // candidate):
                        return True
            return False

        return recurse(n)
