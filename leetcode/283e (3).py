class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cur = 0
        count = 0
        for idx, num in enumerate(nums):
            if num == 0:
                count += 1
            else:
                nums[cur] = num
                cur += 1
        for idx in range(count):
            nums[cur + idx] = 0