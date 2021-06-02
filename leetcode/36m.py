class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [x for x in board]
        columns = []
        for column_index in range(9):
            column = [row[column_index] for row in board]
            columns.append(column)
        grids = []
        for grid_row in range(3):
            for grid_col in range(3):
                grid = []
                for row_offset in range(3):
                    for col_offset in range(3):
                        grid.append(board[3 * grid_row + row_offset][3 * grid_col + col_offset])
                grids.append(grid)

        def is_valid_subset(cells):
            filled_cells = [x for x in cells if x != '.']
            return len(set(filled_cells)) == len(filled_cells)

        return all(is_valid_subset(row) for row in rows) and \
            all(is_valid_subset(column) for column in columns) and \
            all(is_valid_subset(grid) for grid in grids)
