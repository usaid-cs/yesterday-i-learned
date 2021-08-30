class Solution:
    def trailingZeroes(self, n: int) -> int:
        powers_of_5 = []
        for i in range(1, 10):
            powers_of_5.append(5 ** i)
        return sum(n // power_of_5 for power_of_5 in powers_of_5)
