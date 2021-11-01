class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        same_left = -1
        same_right = -1

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                same_left = left
                same_right = right
                break
            elif nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1

        if same_left == same_right == -1:
            return same_left, same_right

        left = same_left
        right = same_right
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                if nums[middle - 1] != target:
                    same_left = middle
                    break
                else:
                    right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1

                left = same_left
        right = same_right
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                if len(nums) == (middle + 1) or nums[middle + 1] != target:
                    same_right = middle
                    break
                else:
                    left = middle + 1
            elif nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1

        return same_left, same_right
