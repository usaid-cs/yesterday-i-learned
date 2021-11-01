"""
You should check if an O is in the edge, because only those are the ones
(along with cells connected to the edge) that cannot be filled
"""
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # is flippable? board
        shadow = [
            [True for x in row]
            for row in board
        ]

        def is_edge(y, x):
            if y == 0 or y == len(board) - 1:
                return True
            if x == 0 or x == len(board[0]) - 1:
                return True
            return False

        def recurse(y, x):
            if board[y][x] != 'O':
                return
            if shadow[y][x] == False:
                # Already been there
                return
            shadow[y][x] = False
            if y > 0:
                recurse(y - 1, x)
            if y < len(board) - 1:
                recurse(y + 1, x)
            if x > 0:
                recurse(y, x - 1)
            if x < len(board[0]) - 1:
                recurse(y, x + 1)

        for y, row in enumerate(board):
            for x, cell in enumerate(row):
                if is_edge(y, x):
                    recurse(y, x)

        for y, row in enumerate(shadow):
            for x, cell in enumerate(row):
                if cell:
                    board[y][x] = 'X'

