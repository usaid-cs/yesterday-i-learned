from functools import lru_cache

# (this is too slow)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jumps = {}

        for idx, num in enumerate(nums):
            jumps[idx] = []

        for idx, num in enumerate(nums):
            for jump_to_idx in range(1, num + 1):
                if idx + jump_to_idx in jumps:
                    jumps[idx + jump_to_idx].append(idx)

        @lru_cache(maxsize=None)
        def recurse(start_idx):
            if start_idx == 0:
                return True
            next_indexes = jumps[start_idx]
            for next_index in next_indexes:
                if recurse(next_index):
                    return True
            return False

        # print(jumps)
        return recurse(len(nums) - 1)