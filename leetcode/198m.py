class Solution:
    def rob(self, nums: List[int]) -> int:
        robs = [0] * len(nums)
        robs[0] = nums[0]
        if len(nums) == 1:
            return robs[0]
        robs[1] = max(nums[0], nums[1])
        if len(nums) == 2:
            return robs[1]

        for i, num in enumerate(nums):
            if i < 2:
                continue
            robs[i] = max(robs[i - 2] + num, robs[i - 1])

        return robs[-1]
