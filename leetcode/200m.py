class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        if not grid[0]:
            return 0
        ys = len(grid)
        xs = len(grid[0])

        islands = 0
        q = []

        def bfs():
            while q:
                y, x = q.pop(0)
                cell = grid[y][x]
                if cell != "1":
                    # couldn't have been on an island
                    continue
                grid[y][x] = "0"
                if 0 <= x - 1 < xs:
                    left = grid[y][x - 1]
                    if left and left == "1":
                        q.append((y, x - 1))
                if 0 <= x + 1 < xs:
                    right = grid[y][x + 1]
                    if right and right == "1":
                        q.append((y, x + 1))
                if 0 <= y - 1 < ys:
                    up = grid[y - 1][x]
                    if up and up == "1":
                        q.append((y - 1, x))
                if 0 <= y + 1 < ys:
                    down = grid[y + 1][x]
                    if down and down == "1":
                        q.append((y + 1, x))
            return 1

        for y in range(ys):
            for x in range(xs):
                if grid[y][x] == "1":
                    q.append((y, x))
                    islands += bfs()
        return islands
