"""
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

    All the visited cells of the path are 0.
    All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).

The length of a clear path is the number of visited cells of this path.
"""
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid and grid[0]:
            return 0

        # i don't know why it can be a global variable in between queue items but ok.
        # note that performance difference is huge between set and list when the grid is big
        travelled_nodes = set()

        # third thing is the number of nodes so far
        q = [(0, 0, 1)]
        while q:
            y, x, length_so_far = q.pop(0)
            if y < 0 or y >= len(grid):
                # not valid coord
                continue
            if x < 0 or x >= len(grid):
                # not valid coord
                continue
            if grid[y][x] == 1:
                # Not a valid path
                continue
            if y == len(grid) - 1 and x == len(grid[0]) - 1:
                return length_so_far

            directions = [
                (y - 1, x - 1),
                (y - 1, x),
                (y - 1, x + 1),
                (y, x - 1),
                (y, x + 1),
                (y + 1, x - 1),
                (y + 1, x),
                (y + 1, x + 1),
            ]
            for direction in directions:
                if direction in travelled_nodes:
                    continue
                travelled_nodes.add(direction)
                q.append((direction[0], direction[1], length_so_far + 1))

        return -1