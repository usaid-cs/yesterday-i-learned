class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        sorted_array = []
        assert len(nums) >= k

        if len(nums) == 1:
            return nums[0]

        def push(num):
            idx = 0
            while idx < len(sorted_array):
                if num < sorted_array[idx]:
                    sorted_array.insert(idx, num)
                    return
                idx += 1
            sorted_array.append(num)

        for num in nums:
            push(num)

        return list(reversed(sorted_array))[k - 1]
