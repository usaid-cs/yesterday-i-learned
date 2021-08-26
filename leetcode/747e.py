class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest, next_largest = float('-inf'), float('-inf')
        largest_idx, next_largest_idx = -1, -1
        for idx, num in enumerate(nums):
            if num > largest:
                next_largest, next_largest_idx = largest, largest_idx
                largest, largest_idx = num, idx
            elif num > next_largest:
                next_largest, next_largest_idx = num, idx
        if largest >= next_largest * 2:
            return largest_idx
        return -1
