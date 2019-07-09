from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        diff = 0
        bought = False
        for price1, price2 in zip([None] + prices, prices + [None]):
            if price1 is None:
                continue
            if price2 is None:
                break
            if not bought:
                if price2 > price1:
                    diff += price2 - price1
                    bought = True
                else:
                    # Well, don't buy losing stock.
                    pass
            else:
                if price2 >= price1:
                    # Well, don't sell winning stock.
                    diff += price2 - price1
                else:
                    # Sell the moment the stock starts to lose.
                    bought = False
        return diff


a = Solution()
assert a.maxProfit([7, 1, 5, 3, 6, 4]) == 7
assert a.maxProfit([1, 2, 3, 4, 5]) == 4
assert a.maxProfit([7, 6, 4, 3, 1]) == 0
