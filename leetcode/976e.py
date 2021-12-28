class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        nums = nums[::-1]

        while len(nums) >= 3:
            if nums[0] < (nums[1] + nums[2]):
                return nums[0] + nums[1] + nums[2]
            else:
                nums.pop(0)
        return 0
