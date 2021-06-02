class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        supposed_heights = sorted(heights)
        diu = 0
        for a, b in zip(supposed_heights, heights):
            if a != b:
                diu += 1
        return diu
