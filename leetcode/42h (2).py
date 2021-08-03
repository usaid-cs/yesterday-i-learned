class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left_maxes = [0] * len(height)
        right_maxes = [0] * len(height)

        left_maxes[0] = height[0]
        for idx, height_at_idx in enumerate(height[1:], start=1):
            left_maxes[idx] = max(left_maxes[idx - 1], height_at_idx)

        right_maxes[-1] = height[-1]
        idx = len(height) - 2
        while idx >= 0:
            height_at_idx = height[idx]
            right_maxes[idx] = max(right_maxes[idx + 1], height_at_idx)
            idx -= 1

        # print(left_maxes)
        # print(right_maxes)
        # print([min(l, r) - h for l, r, h in zip(left_maxes, right_maxes, height)])

        return sum(min(l, r) - h for l, r, h in zip(left_maxes, right_maxes, height))
