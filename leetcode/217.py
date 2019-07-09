from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # return len(nums) != len(set(nums))  # Cheater version
        original_len = len(nums)
        found = set()
        for num in nums:
            found.add(num)
        return len(found) != original_len


a = Solution()
assert a.containsDuplicate([1, 2, 3, 4]) == False
assert a.containsDuplicate([1, 2, 3, 1]) == True

import random
b = [random.randint(0, 1000000) for _ in range(1000000)]
assert a.containsDuplicate(b) == True
