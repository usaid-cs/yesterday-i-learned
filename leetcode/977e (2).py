class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1

        result = []
        while left <= right:
            num_left = nums[left] ** 2
            num_right = nums[right] ** 2
            if num_left >= num_right:
                result.insert(0, num_left)
                left += 1
            else:
                result.insert(0, num_right)
                right -= 1
        return result
