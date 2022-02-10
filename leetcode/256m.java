class Solution {
    public int minCost(int[][] costs) {
        for (int house = 1; house < costs.length; house++) {
            for (int color = 0; color < costs[house].length; color++) {
                if (color == 0) { // R
                    costs[house][color] += Math.min(costs[house - 1][1], costs[house - 1][2]);
                } else if (color == 1) { // G
                    costs[house][color] += Math.min(costs[house - 1][0], costs[house - 1][2]);
                } else if (color == 2) { // B
                    costs[house][color] += Math.min(costs[house - 1][0], costs[house - 1][1]);
                }
            }
        }
        return Math.min(Math.min(costs[costs.length - 1][0], costs[costs.length - 1][1]), costs[costs.length - 1][2]);
    }
}
