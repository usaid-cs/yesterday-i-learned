# This is bubble sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        while True:
            did_something = False
            for idx in range(len(nums) - 1):
                num1, num2 = nums[idx], nums[idx + 1]
                if num1 > num2:
                    nums[idx], nums[idx + 1] = nums[idx + 1], nums[idx]
                    did_something = True
            if not did_something:
                return nums
