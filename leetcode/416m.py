class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort()
        sum_of = sum(nums)
        if sum_of % 2:
            return False
        target = sum_of // 2

        memo = {}

        def recurse(cur, other_nums):
            if sum(other_nums) in memo:
                return memo[sum(other_nums)]

            if cur == target:
                return True
            if cur > target:
                return False

            for idx, num in enumerate(other_nums):
                rest = other_nums[:idx] + other_nums[idx + 1:]
                result = recurse(num + cur, rest)
                memo[sum(rest)] = result
                if result:
                    return True
            return False

        return recurse(0, nums)
