# TODO
class Solution:
    def numSquares(self, n: int) -> int:
        def ps(root):
            return root * root

        if n in [0, 1]:
            return n

        square_roots_to_use = 1
        total = sum(ps(x) for x in range(square_roots_to_use))


print(Solution().numSquares(12))