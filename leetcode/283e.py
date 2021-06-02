class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_zeroes = 0
        i = 0
        while i < len(nums) - 1:
            num = nums[i]
            if num == 0:
                nums.pop(i)
                num_zeroes += 1
            else:
                i += 1
        for i in range(num_zeroes):
            nums.append(0)
