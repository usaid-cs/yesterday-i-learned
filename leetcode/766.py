def get_col(matrix, col: int):
    buffer = []
    for row in matrix:
        try:
            if row[col] is not None:
                buffer.append(row[col])
        except IndexError:
            pass
    return buffer


def col_contains_one_number(matrix, col_idx):
    col = get_col(matrix, col_idx)
    print(set(col))
    return len(set(col)) <= 1


class Solution:
    def isToeplitzMatrix(self, matrix) -> bool:
        row_count = len(matrix)
        if not matrix:
            return True
        if not matrix[0] or len(matrix[0]) == 1:
            return True
        for idx, row in enumerate(matrix):
            for _ in range(row_count - idx - 1):
                row.insert(0, None)
        print(matrix)
        cols_count = max(row_count * 2, len(matrix[0]))
        return all(
            col_contains_one_number(matrix, col_idx)
            for col_idx in range(cols_count))
