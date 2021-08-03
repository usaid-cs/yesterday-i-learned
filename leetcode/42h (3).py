"""

"""
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left = 0
        right = len(height) - 1

        ans = 0

        left_max = height[left]
        right_max = height[right]
        while left < right:
            if height[left] < height[right]:
                if height[left] >= right_max:
                    left_max = height[left]
                else:
                    ans += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += right_max - height[right]
                right -= 1

        return ans
