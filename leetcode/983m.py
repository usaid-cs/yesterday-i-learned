"""
You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.

Train tickets are sold in three different ways:

    a 1-day pass is sold for costs[0] dollars,
    a 7-day pass is sold for costs[1] dollars, and
    a 30-day pass is sold for costs[2] dollars.

The passes allow that many days of consecutive travel.

    For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given list of days.
"""
# The trick here is to compute from the last day to the first day.
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        day_max = 365
        day_costs = [None for _ in range(day_max + 1)]

        day_pass = costs[0]
        week_pass = costs[1]
        month_pass = costs[2]

        def dp(day_number):
            if day_number > day_max:
                return 0  # you start the problem with $0
            if day_number not in days:
                return dp(day_number + 1)
            if day_costs[day_number] is not None:
                return day_costs[day_number]
            day_costs[day_number] = min(
                dp(day_number + 1) + day_pass,
                dp(day_number + 7) + week_pass,
                dp(day_number + 30) + month_pass,
            )
            return day_costs[day_number]

        return dp(1)
