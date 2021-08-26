class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointer2 = len(numbers) - 1
        pointer1 = 0
        while True:
            current_sum = numbers[pointer1] + numbers[pointer2]
            if current_sum == target:
                return [pointer1 + 1, pointer2 + 1]
            elif current_sum < target:
                pointer1 += 1
            elif current_sum > target:
                pointer2 -= 1
