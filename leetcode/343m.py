"""
Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

Return the maximum product you can get.
"""
class Solution:
    def integerBreak(self, n: int) -> int:
        max_products = [0] * (n + 1)
        max_products[1] = 1

        if n < 4:
            for i in range(2, n + 1):
                max_at_i = 0
                for j in range(1, i):
                    max_at_i = max(max_at_i, max_products[j] * (i - j))
                max_products[i] = max_at_i
            return max_products[n]
        else:
            for i in range(2, n + 1):
                max_at_i = i
                for j in range(1, i):
                    max_at_i = max(max_at_i, max_products[j] * (i - j))
                max_products[i] = max_at_i
            return max_products[n]
