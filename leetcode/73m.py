class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroes = []
        for y, row in enumerate(matrix):
            for x, val in enumerate(row):
                print((x, y), val)
                if val == 0:
                    zeroes.append((x, y))
        if not matrix:
            return
        for (x, y) in zeroes:
            for x_prime in range(0, len(matrix[0])):
                matrix[y][x_prime] = 0
            for y_prime in range(0, len(matrix)):
                matrix[y_prime][x] = 0