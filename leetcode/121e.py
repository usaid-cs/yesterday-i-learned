# Dumbass n^2 solution (do not use)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for idx1 in range(len(prices)):
            for idx2 in range(idx1, len(prices)):
                max_profit = max(max_profit, prices[idx2] - prices[idx1])
        return max_profit
