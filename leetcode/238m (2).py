class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [0] * len(nums)
        r = [0] * len(nums)
        l[0] = 1
        r[-1] = 1

        for idx, num in enumerate(nums):
            if idx < len(nums) - 1:
                l[idx + 1] = l[idx] * num

        idx = len(nums) - 1
        while idx > 0:
            num = nums[idx]
            r[idx - 1] = r[idx] * num
            idx -= 1

        return [x * y for x, y in zip(l, r)]
