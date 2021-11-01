"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def recurse(y, x, match_rest=word):
            # print(board, match_rest)
            if not match_rest:
                return True
            if not (0 <= y <= len(board) - 1):
                return False
            if not (0 <= x <= len(board[0]) - 1):
                return False
            letter = board[y][x]
            if board[y][x] == '':
                return False
            board[y][x] = ''  # make unmatchable
            if match_rest[0] != letter:
                board[y][x] = letter  # backtrack
                return False
            if recurse(y - 1, x, match_rest[1:]):
                board[y][x] = letter  # backtrack
                return True
            if recurse(y + 1, x, match_rest[1:]):
                board[y][x] = letter  # backtrack
                return True
            if recurse(y, x - 1, match_rest[1:]):
                board[y][x] = letter  # backtrack
                return True
            if recurse(y, x + 1, match_rest[1:]):
                board[y][x] = letter  # backtrack
                return True
            board[y][x] = letter  # backtrack
            return False

        for y, row in enumerate(board):
            for x, letter in enumerate(row):
                if recurse(y, x):
                    return True
        return False