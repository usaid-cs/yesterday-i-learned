class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) <= 1:
            print([])
            return 0
        sums = []
        for idx, price in enumerate(prices):
            if idx == 0:
                sums.append(price)
                continue
            prev_price = prices[idx - 1]
            if price - prev_price > 0:
                sums.append(prev_price + price)
            else:
                sums.append(price)

        print(sums)
        return max(sums)


a = Solution()
assert a.maxProfit([]) == 0
assert a.maxProfit([1234]) == 0
assert a.maxProfit([0, 0]) == 0
assert a.maxProfit([0, 1234]) == 1234
assert a.maxProfit([7, 1, 5, 3, 6, 4]) == 5
assert a.maxProfit([1234, 0]) == 0
assert a.maxProfit([7, 6, 4, 3, 1]) == 0

