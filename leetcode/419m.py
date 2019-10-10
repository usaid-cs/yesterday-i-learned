from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board:
            return 0
        if not board[0]:
            return 0
        # Fuck you
        ships = []

        for y, row in enumerate(board):
            for x, cell in enumerate(row):
                if cell != 'X':
                    continue
                for ship in ships:
                    if (x, y) in ship:
                        break
                    if (x - 1, y) in ship:
                        ship.append((x, y))
                        break
                    if (x + 1, y) in ship:
                        ship.append((x, y))
                        break
                    if (x, y - 1) in ship:
                        ship.append((x, y))
                        break
                    if (x, y + 1) in ship:
                        ship.append((x, y))
                        break
                else:
                    ships.append([(x, y)])

        print(ships)
        return len(ships)


a = Solution()

board = [["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]
assert a.countBattleships(board) == 2

board = [["X", "X", "X", "X"], [".", ".", ".", "."], [".", ".", ".", "X"]]
assert a.countBattleships(board) == 2

board = [["X", "X", ".", "."], [".", ".", "X", "X"], ["X", "X", ".", "."]]
assert a.countBattleships(board) == 3