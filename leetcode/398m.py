import random

class Solution:

    def __init__(self, nums: List[int]):
        self.num_map = {}
        for idx, num in enumerate(nums):
            if num in self.num_map:
                self.num_map[num].append(idx)
            else:
                self.num_map[num] = [idx]

    def pick(self, target: int) -> int:
        assert target in self.num_map
        return random.choice(self.num_map[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)22
