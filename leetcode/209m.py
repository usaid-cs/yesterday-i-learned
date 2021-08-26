class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        current_subarray = None
        head = 0
        tail = 1
        while head < len(nums):
            subarray = nums[head:tail]
            subarray_sum = sum(subarray)
            if subarray_sum >= target:
                if current_subarray is None or len(subarray) < len(current_subarray):
                    current_subarray = subarray
                head += 1
            elif subarray_sum < target:
                tail += 1
            if tail > len(nums):
                break
        if current_subarray is None:
            return 0
        return len(current_subarray)
