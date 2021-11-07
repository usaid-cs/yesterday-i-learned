"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [
            [0 for _ in range(n)]
            for _ in range(m)]

        for row in grid:
            row[0] = 1

        for idx, cell in enumerate(grid[0]):
            grid[0][idx] = 1

        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if y < 1 or x < 1:
                    continue
                grid[y][x] = grid[y - 1][x] + grid[y][x - 1]

        return grid[-1][-1]
