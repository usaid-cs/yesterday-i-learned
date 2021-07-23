from typing import List

# Scan left, scan right, subtract actual heights, sum them all up


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left_heights = [0] * len(height)
        right_heights = [0] * len(height)

        left_max = 0
        for idx, cur in enumerate(height):
            left_heights[idx] = max(left_max, cur)
            if cur > left_max:
                left_max = cur

        right_max = 0
        for flip, cur in enumerate(reversed(height)):
            idx = len(height) - flip - 1
            right_heights[idx] = max(right_max, cur)
            if cur > right_max:
                right_max = cur

        print(left_heights, right_heights)
        mins = []
        for idx, pairs in enumerate(zip(left_heights, right_heights)):
            mins.append(min(pairs) - height[idx])
        print(mins)
        return sum(mins)


a = Solution()
assert a.trap([4, 2, 3]) == 1
assert a.trap([1, 0, 1]) == 1
assert a.trap([1]) == 0
assert a.trap([2, 1, 2]) == 1
assert a.trap([0, 0, 0]) == 0
assert a.trap([0, 1, 0]) == 0
assert a.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
