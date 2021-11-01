class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) -1

        while left < right:
            summed = numbers[left] + numbers[right]
            if summed == target:
                return [left + 1, right + 1]
            if summed < target:
                left += 1
            else:
                right -= 1
        return [-1, -1]
