class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        def recurse(row_idx):
            if row_idx <= 0:
                return [1]
            prev_row = recurse(row_idx - 1)
            prev_cell_count = len(prev_row)
            row = [1] * (prev_cell_count + 1)
            for idx in range(1, len(row)):
                try:
                    row[idx] = prev_row[idx - 1] + prev_row[idx]
                except IndexError:
                    row[idx] = prev_row[idx - 1]
            return row

        return recurse(rowIndex)
