# This MF can be achieved with this one line:
# return min(len(set(candies)), len(candies) // 2)
# https://leetcode.com/problems/distribute-candies/discuss/306554/Python-one-line-bieats-96


class Solution:
    def distributeCandies(self, candies) -> int:
        candies = sorted(candies)
        brother = []
        brother_len = 0
        sister = []
        sister_len = 0
        if not candies:
            return 0
        expected_num = len(candies) / 2
        for candy in candies:
            if sister_len >= expected_num:
                brother.append(candy)
                brother_len += 1
            elif brother_len >= expected_num:
                sister.append(candy)
                sister_len += 1
            elif sister and sister[-1] == candy:
                brother.append(candy)
                brother_len += 1
            else:
                sister.append(candy)
                sister_len += 1
        return len(set(sister))