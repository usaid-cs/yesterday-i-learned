from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or k == 0:
            return
        for _ in range(k):
            last = nums.pop()
            nums.insert(0, last)


a = Solution()
arr = [1, 2, 3, 4, 5, 6, 7]
a.rotate(arr, k=3)
assert arr == [5, 6, 7, 1, 2, 3, 4]
arr = [1, 2]
a.rotate(arr, k=1)
assert arr == [2, 1]
