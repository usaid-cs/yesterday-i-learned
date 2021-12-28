"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # Tell yourself it is impossible to have a coin worth 0

        for subamount in range(1, amount + 1):
            for coin in coins:
                remainder = subamount - coin
                if remainder < 0:
                    continue
                dp[subamount] = min(dp[subamount], dp[remainder] + 1)
        if dp[-1] > amount:
            return -1
        return dp[-1]