import heapq

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        heapq.heapify(nums)
        max_len = 0
        len = 0
        prev = None
        while nums:
            cur = heapq.heappop(nums)
            if prev is None:
                len += 1
                max_len = max(max_len, len)
            elif cur == prev + 1:
                len += 1
                max_len = max(max_len, len)
            elif cur == prev:
                continue
            else:
                # sequence restarts here
                len = 1
            prev = cur
        return max_len
