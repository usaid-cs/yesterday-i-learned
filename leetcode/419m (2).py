"""
lol it's the same as 200 because there are no adjacent ships to fuck up
your algorithm
"""
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        def mark_ship(y, x, ship_number=1):
            if y < 0 or y > len(board) - 1:
                return False
            if x < 0 or x > len(board[0]) - 1:
                return False
            if board[y][x] != 'X':
                return False
            board[y][x] = ship_number
            mark_ship(y + 1, x, ship_number)
            mark_ship(y - 1, x, ship_number)
            mark_ship(y, x + 1, ship_number)
            mark_ship(y, x - 1, ship_number)
            return True

        ship_count = 0
        for y, row in enumerate(board):
            for x, cell in enumerate(row):
                if cell == '.':
                    continue
                if cell == 'X':
                    mark_ship(y, x, ship_count + 1)
                    ship_count += 1
        return ship_count
