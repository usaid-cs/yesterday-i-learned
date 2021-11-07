"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            nums = [board[row][i] for i in range(9) if board[row][i] != '.']
            if len(nums) != len(set(nums)):
                return False

        for col in range(9):
            nums = [board[x][col] for x in range(9) if board[x][col] != '.']
            if len(nums) != len(set(nums)):
                return False

        for start_y in range(3):
            for start_x in range(3):
                nums = []
                for y_offset in range(3):
                    for x_offset in range(3):
                        y = start_y * 3 + y_offset
                        x = start_x * 3 + x_offset
                        if board[y][x] != '.':
                            nums.append(board[y][x])
                if len(nums) != len(set(nums)):
                    return False
        return True