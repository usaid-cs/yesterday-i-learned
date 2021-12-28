class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        list_size = []
        for row in mat:
            list_size.extend(row)
        if len(list_size) != r * c:
            return mat

        ans = []
        while list_size:
            row_buffer = []
            while len(row_buffer) < c:
                row_buffer.append(list_size.pop(0))
            ans.append(row_buffer)
        return ans