class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        def max_subarray(numbers):
            """Find the largest sum of any contiguous subarray."""
            best_sum = 0  # or: float('-inf')
            current_sum = 0
            for x in numbers:
                current_sum = max(0, current_sum + x)
                best_sum = max(best_sum, current_sum)
            return best_sum

        price_changes = [0]
        for idx in range(len(prices) - 1):
            price_changes.append(prices[idx + 1] - prices[idx])

        return max_subarray(price_changes)
