class Solution:
    def islandPerimeter(self, grid) -> int:
        def point_perimeter(x, y):
            point = grid[y][x]
            if point == 0:
                # A cell with nothing is not a perimeter
                return 0
            sides = 0

            if x == 0:
                sides += 1
            else:
                left = grid[y][x - 1]
                if left == 0:
                    sides += 1
            if x == len(grid[y]) - 1:
                sides += 1
            else:
                right = grid[y][x + 1]
                if right == 0:
                    sides += 1
            if y == 0:
                sides += 1
            else:
                top = grid[y - 1][x]
                if top == 0:
                    sides += 1
            if y == len(grid) - 1:
                sides += 1
            else:
                bottom = grid[y + 1][x]
                if bottom == 0:
                    sides += 1
            return sides

        edges = 0
        for y, row in enumerate(grid):
            for x in range(len(row)):
                edges += point_perimeter(x, y)
        return edges


grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
print(Solution().islandPerimeter(grid))