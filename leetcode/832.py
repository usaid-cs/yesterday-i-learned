from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in range(len(A)):
            row = list(reversed(A[i]))
            A[i] = [1 if x == 0 else 0 for x in row]

        return A


a = Solution()
print(a.flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
