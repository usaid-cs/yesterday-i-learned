import json


class Solution:
    def matrixReshape(self, nums, r: int, c: int):
        if not nums:
            return nums
        rows_orig = len(nums)
        cols_orig = len(nums[0])
        if rows_orig * cols_orig != r * c:
            return nums

        lst = []
        for row in nums:
            lst.extend(row)

        new_matrix = []
        for row_idx in range(r):
            new_row = lst[row_idx * c:row_idx * c + c]
            new_matrix.append(new_row)
        return new_matrix


nums = [[1, 2], [3, 4]]
print(json.dumps(Solution().matrixReshape(nums, 1, 4)))