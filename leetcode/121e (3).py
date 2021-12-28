class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_diff = float('-inf')
        for price in prices:
            min_price = min(min_price, price)
            max_diff = max(max_diff, price - min_price)
        return max_diff
