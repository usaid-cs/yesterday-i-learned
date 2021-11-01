class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        
        result = []
        while left <= right:
            left_num = nums[left] ** 2
            right_num = nums[right] ** 2
            if left_num > right_num:
                result.insert(0, left_num)
                left += 1
            else:
                result.insert(0, right_num)
                right -= 1
        return result
