class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)

        nums1 = nums[:-1]
        robs1 = [0] * len(nums1)
        robs1[0] = nums1[0]
        robs1[1] = max(nums1[0], nums1[1])
        for i, num in enumerate(nums1):
            if i < 2:
                continue
            robs1[i] = max(robs1[i - 2] + num, robs1[i - 1])

        nums2 = nums[1:]
        robs2 = [0] * len(nums2)
        robs2[0] = nums2[0]
        robs2[1] = max(nums2[0], nums2[1])
        for i, num in enumerate(nums2):
            if i < 2:
                continue
            robs2[i] = max(robs2[i - 2] + num, robs2[i - 1])

        return max(robs1[-1], robs2[-1])
