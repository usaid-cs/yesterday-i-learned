from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = 0
        ops = 0
        while idx < len(nums) - ops:
            num = nums[idx]
            if num == 0:
                nums.remove(0)
                nums.append(0)
                ops += 1
            else:
                idx += 1


a = Solution()
z = []
a.moveZeroes(z)
assert z == []

z = [0, 1, 0, 3, 12]
a.moveZeroes(z)
assert z == [1, 3, 12, 0, 0]
