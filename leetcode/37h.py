from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        all_digits = set(["1", "2", "3", "4", "5", "6", "7", "8", "9"])

        row_possibilities = [
            set(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
            for _ in range(9)
        ]

        col_possibilities = [
            set(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
            for _ in range(9)
        ]

        subgrid_possibilities = []
        for _ in range(3):
            buffer = []
            for __ in range(3):
                buffer.append(set(["1", "2", "3", "4", "5", "6", "7", "8", "9"]))
            subgrid_possibilities.append(buffer)

        def is_complete():
            for row in board:
                for cell in row:
                    if cell == '.':
                        return False
            return True

        def get_row(y):
            return [i for i in board[y] if i != '.']

        def get_col(x):
            digits = [board[i][x] for i in range(9)]
            return [i for i in digits if i != '.']

        def get_subgrid(y, x):
            if 0 <= y <= 2:
                rows = [board[i] for i in range(0, 3)]
            elif 3 <= y <= 5:
                rows = [board[i] for i in range(3, 6)]
            elif 6 <= y <= 8:
                rows = [board[i] for i in range(6, 9)]

            digits = []
            for row in rows:
                if 0 <= x <= 2:
                    for i in range(0, 3):
                        digits.append(row[i])
                if 3 <= x <= 5:
                    for i in range(3, 6):
                        digits.append(row[i])
                if 6 <= x <= 8:
                    for i in range(6, 9):
                        digits.append(row[i])
            return [i for i in digits if i != '.']

        def get_missing(digits):
            buffer = []
            for digit in all_digits:
                if digit not in digits:
                    buffer.append(digit)
            return buffer

        def get_options(y, x):
            # row_vals = get_missing(get_row(y))
            # col_vals = get_missing(get_col(x))
            # subgrid_vals = get_missing(get_subgrid(y, x))
            row_vals = row_possibilities[y]
            col_vals = col_possibilities[x]
            subgrid_vals = subgrid_possibilities[y // 3][x // 3]
            possible = set(row_vals) & set(col_vals) & set(subgrid_vals)
            return list(possible)

        while not is_complete():
            for x in range(9):
                col_vals = get_col(x)
                for val in col_vals:
                    if val in col_possibilities[x]:
                        col_possibilities[x].remove(val)

            for y in range(9):
                row_vals = get_row(y)
                for val in row_vals:
                    if val in row_possibilities[y]:
                        row_possibilities[y].remove(val)

            for y in range(9):
                for x in range(9):
                    subgrid_vals = get_subgrid(y, x)
                    for val in subgrid_vals:
                        try:
                            if val in subgrid_possibilities[y // 3][x // 3]:
                                subgrid_possibilities[y // 3][x // 3].remove(val)
                        except IndexError:
                            print(y, x)

            for y, row in enumerate(board):
                for x, cell in enumerate(row):
                    if board[y][x] == '.':
                        options = get_options(y, x)
                        if len(options) == 1:
                            board[y][x] = options[0]
        return board

a = Solution()
print(a.solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))
print(a.solveSudoku([[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]))
