class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        robs = [0] * (max(nums) + 1)
        for i in nums:
            robs[i] += i

        robs[1] = max(robs[0], robs[1])
        for i, num in enumerate(robs):
            if i < 2:
                continue
            robs[i] = max(robs[i - 2] + num, robs[i - 1])
        return robs[-1]
