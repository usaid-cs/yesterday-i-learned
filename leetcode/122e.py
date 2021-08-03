# If you know it's going to go up tomorrow then just buy lol
# If you know it's going to drop tomorrow then just sell lol
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        prev_buy_point = None
        bought_in = False
        for price1, price2 in zip(prices[:-1], prices[1:]):
            if bought_in:
                if price2 < price1:
                    # sell today
                    bought_in = False
                    max_profit += (price1 - prev_buy_point)
                    prev_buy_point = 0
            elif not bought_in:
                if price2 > price1:
                    # buy today
                    bought_in = True
                    prev_buy_point = price1

        if bought_in:
            # don't forget to sell if you're still hodling at the end
            max_profit += (price2 - prev_buy_point)
        return max_profit
