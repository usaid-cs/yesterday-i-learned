"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.
"""
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        planted = 0

        def get_left_right(idx):
            if idx == 0:
                left = 0
            else:
                left = flowerbed[idx - 1]
            if idx == len(flowerbed) - 1:
                right = 0
            else:
                right = flowerbed[idx + 1]
            return left, right

        for idx, plot in enumerate(flowerbed):
            if plot != 0:
                continue

            plot_left, plot_right = get_left_right(idx)
            if plot_left == 0 and plot_right == 0:
                flowerbed[idx] = 1
                planted += 1
        return (planted >= n)
