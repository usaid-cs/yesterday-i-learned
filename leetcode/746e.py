class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        min_costs = [0] * len(cost)

        min_costs[0] = cost[0]
        min_costs[1] = cost[1]
        for i in range(2, len(cost)):
            min_costs[i] = min(min_costs[i - 1],
                               min_costs[i - 2]) + cost[i]
        return min_costs[-1]
