from typing import List


def is_valid_set(vals):
    assert len(vals) == 9, 'go fuck yourself'
    has_nums = set()
    for val in vals:
        if val in has_nums:
            return False
        if val != '.':
            has_nums.add(val)
    return True


def check_rows(board):
    for row in board:
        if not is_valid_set(row):
            return False
    return True


def check_columns(board):
    for idx in range(9):
        col = [row[idx] for row in board]
        if not is_valid_set(col):
            return False
    return True


def get_quad(board, x, y):
    vals = []
    for i in range(3):
        for j in range(3):
            vals.append(board[y + j][x + i])
    return vals


def check_grids(board):
    quad_x = [0, 3, 6]
    quad_y = [0, 3, 6]
    for x in quad_x:
        for y in quad_y:
            vals = get_quad(board, x, y)
            if not is_valid_set(vals):
                return False
    return True


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not check_rows(board):
            return False
        if not check_columns(board):
            return False
        return check_grids(board)


a = Solution()
grid = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
assert a.isValidSudoku(grid) is True

grid = [["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
assert a.isValidSudoku(grid) is False