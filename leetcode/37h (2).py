# Backtracking
class Solution:
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        def get_box(row, col):
            return boxes[row // 3 * 3 + col // 3]

        def is_valid(try_str, row, col):
            try_str = str(try_str)
            if try_str in rows[row]:
                return False
            if try_str in cols[col]:
                return False
            if try_str in get_box(row, col):
                return False
            return True

        def add(num_str, row, col):
            board[row][col] = num_str
            rows[row].add(num_str)
            cols[col].add(num_str)
            get_box(row, col).add(num_str)

        def remove(num_str, row, col):
            board[row][col] = '.'
            rows[row].remove(num_str)
            cols[col].remove(num_str)
            get_box(row, col).remove(num_str)

        # init the rows cols and boxes
        for row_idx, row in enumerate(board):
            for col_idx, cell in enumerate(row):
                rows[row_idx].add(str(cell))
                cols[col_idx].add(str(cell))
                box = get_box(row_idx, col_idx)
                box.add(str(cell))

        def fill_cell(row, col):
            if col >= 9:
                # wrap around
                row += 1
                col = 0
            if row == 9:
                # we came from (8, 8) so we are done
                return True

            if board[row][col] != '.':
                # It's filled, go do the next cell
                return fill_cell(row, col + 1)

            for try_num in range(1, 10):
                try_str = str(try_num)
                if not is_valid(try_str, row, col):
                    continue
                add(try_str, row, col)
                solved = fill_cell(row, col + 1)
                if solved:
                    return solved
                else:
                    remove(try_str, row, col)
            return False

        fill_cell(0, 0)
