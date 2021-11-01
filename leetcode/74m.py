"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1
        while top <= bottom:
            middle = (top + bottom) // 2
            if bottom == middle:
                break
            first_num = matrix[middle][0]
            last_num = matrix[middle][-1]
            # above = matrix[top][0]
            # below = matrix[bottom][-1]
            if target == first_num: # in [first_num, above, below]:
                return True
            if first_num <= target <= last_num:
                break
            if target < first_num:
                bottom = middle - 1
            elif target > first_num:
                top = middle + 1

        row = matrix[middle]
        left = 0
        right = len(row) - 1
        while left <= right:
            middle = (left + right) // 2
            if row[middle] == target:
                return True
            if row[middle] < target:
                left = middle + 1
            elif row[middle] > target:
                right = middle - 1
        return False
