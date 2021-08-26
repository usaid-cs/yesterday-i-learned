# You got the correct solution in one go and you don't know how
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        left_ptr = 0
        right_ptr = len(height) - 1

        max_volume = 0

        while left_ptr < right_ptr:
            height_left = height[left_ptr]
            height_right = height[right_ptr]
            volume = min(height_left, height_right) * (right_ptr - left_ptr)
            if volume > max_volume:
                max_volume = volume
            if height_left >= height_right:
                right_ptr -= 1
            else:
                left_ptr += 1
        return max_volume
