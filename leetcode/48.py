class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        def transpose():
            n = len(matrix)
            for y, row in enumerate(matrix):
                for x, cell in enumerate(row):
                    if x < y:
                        continue
                    matrix[y][x], matrix[x][y] = matrix[x][y], matrix[y][x]

        def reverse():
            for y, row in enumerate(matrix):
                matrix[y] = row[::-1]

        # This rotates it 90 degrees clockwise
        transpose()
        reverse()

        # This rotates it 90 degrees counterclockwise
        reverse()
        transpose()
