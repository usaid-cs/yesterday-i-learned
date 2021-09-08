class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        answer_grid = [[float('inf') for x in y] for y in grid]
        answer_grid[0][0] = 0

        for row_idx, row in enumerate(grid):
            for col_idx, cell in enumerate(row):
                if row_idx > 0:
                    up_cell = answer_grid[row_idx - 1][col_idx]
                else:
                    up_cell = float('inf')
                if col_idx > 0:
                    left_cell = answer_grid[row_idx][col_idx - 1]
                else:
                    left_cell = float('inf')

                answer_grid[row_idx][col_idx] = min(
                    answer_grid[row_idx][col_idx] + cell,
                    up_cell + cell,
                    left_cell + cell,
                )

        return answer_grid[-1][-1]
