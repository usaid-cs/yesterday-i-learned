RIGHT = 1
DOWN = 2
LEFT = 3
UP = 4


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        start_y = 0
        start_x = 0
        direction = RIGHT
        top = 1
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        y = start_y
        x = start_x
        cells = [matrix[0][0]]
        while True:
            if len(cells) == len(matrix) * len(matrix[0]):
                break
            if direction == RIGHT:
                if x < right:
                    x += 1
                else:
                    direction = DOWN
                    right -= 1
                    continue
            elif direction == DOWN:
                if y < bottom:
                    y += 1
                else:
                    direction = LEFT
                    bottom -= 1
                    continue
            elif direction == LEFT:
                if x > left:
                    x -= 1
                else:
                    direction = UP
                    left += 1
                    continue
            elif direction == UP:
                if y > top:
                    y -= 1
                else:
                    direction = RIGHT
                    top += 1
                    continue
            next_cell = matrix[y][x]
            cells.append(next_cell)
            if len(cells) == len(matrix) * len(matrix[0]):
                break
        return cells