class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def has_edge(y, x):
            if y == 0 or y == len(board) - 1:
                return True
            return x == 0 or x == len(board[0]) - 1

        def recurse(y, x):
            cell = board[y][x]
            if cell == 'X':
                return
            if has_edge(y, x):
                recurse2(y, x)

        def recurse2(y, x):
            if not 0 <= y <= len(board) - 1:
                return
            if not 0 <= x <= len(board[0]) - 1:
                return
            if new_board[y][x]:
                return
            cell = board[y][x]
            if cell == 'X':
                return

            new_board[y][x] = True
            recurse2(y - 1, x)
            recurse2(y + 1, x)
            recurse2(y, x - 1)
            recurse2(y, x + 1)

        new_board = [
            [False for _ in row]
            for row in board
        ]
        for y, row in enumerate(board):
            for x, cell in enumerate(row):
                if cell == 'X':
                    continue

                recurse(y, x)

        for y, row in enumerate(board):
            for x, cell in enumerate(row):
                if cell == 'O':
                    if not new_board[y][x]:
                        board[y][x] = 'X'
        return board