from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        cur = 0
        sums = []
        for num in nums:
            sums.append(max(num, cur + num))
            cur = max(num, cur + num)
        print(sums)
        return max(sums)


a = Solution()
assert a.maxSubArray([]) == 0
assert a.maxSubArray([1]) == 1
assert a.maxSubArray([1, 2]) == 3
assert a.maxSubArray([1, -2, 3]) == 3
assert a.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
