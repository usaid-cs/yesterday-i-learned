class Solution:
    def tribonacci(self, n: int) -> int:
        tribs = [0] * (n + 3)
        tribs[1] = 1
        tribs[2] = 1
        for i in range(3, n + 1):
            tribs[i] = tribs[i - 1] + tribs[i - 2] + tribs[i - 3]
        return tribs[n]
