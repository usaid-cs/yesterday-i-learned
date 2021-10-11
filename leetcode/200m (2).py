class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(y, x):
            if y < 0 or y > len(grid) - 1:
                return 0
            if x < 0 or x > len(grid[0]) - 1:
                return 0
            if grid[y][x] == '0':
                return 0
            grid[y][x] = '0'  # mark as eaten
            dfs(y + 1, x)
            dfs(y - 1, x)
            dfs(y, x + 1)
            dfs(y, x - 1)
            return 1

        max_island = 0
        for idx, row in enumerate(grid):
            for idx2, cell in enumerate(row):
                max_island += dfs(idx, idx2)
        return max_island
