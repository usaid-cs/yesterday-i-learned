class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        found_zeroes = []
        for y, row in enumerate(matrix):
            for x, cell in enumerate(row):
                if cell == 0:
                    found_zeroes.append([y, x])

        print(found_zeroes)
        for y, x in found_zeroes:
            for y2, row in enumerate(matrix):
                row[x] = 0
                if y == y2:
                    for idx, val in enumerate(row):
                        row[idx] = 0
        return matrix