from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ln = len(nums)
        if ln <= 1:
            return ln
        idx = 0
        while idx < ln - 1:
            item = nums[idx]
            item2 = nums[idx + 1]
            if item == item2:
                nums.pop(idx + 1)
                ln -= 1
            else:
                idx += 1
        return ln


a = Solution()
arr = [1, 2, 3]
rel = a.removeDuplicates(arr)
assert arr == [1, 2, 3]
assert rel == 3