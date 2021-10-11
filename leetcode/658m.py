from heapq import heapify, heappush, heappop

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        diffs = []

        for num in arr:
            heappush(diffs, (abs(num - x), num))

        ans = []
        for _ in range(k):
            diff, n = heappop(diffs)
            ans.append(n)

        return sorted(ans)
