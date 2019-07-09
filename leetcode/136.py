from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        assert nums, '"non-empty" my ass'
        s = {}
        for n in nums:
            if n in s:
                s[n] += 1
            else:
                s[n] = 1
        for k, v in s.items():
            if v == 1:
                return k
        raise ValueError('fuck')