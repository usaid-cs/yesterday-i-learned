"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
"""
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(y, x):
            if y < 0 or y > len(grid) - 1:
                return 0
            if x < 0 or x > len(grid[0]) - 1:
                return 0
            if grid[y][x] == 0:
                return 0
            grid[y][x] = 0  # mark as eaten
            return 1 + sum([
                dfs(y + 1, x),
                dfs(y - 1, x),
                dfs(y, x + 1),
                dfs(y, x - 1),
            ])

        max_island = 0
        for idx, row in enumerate(grid):
            for idx2, cell in enumerate(row):
                max_island = max(max_island, dfs(idx, idx2))
        return max_island
