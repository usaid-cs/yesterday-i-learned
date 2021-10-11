"""
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

    Each child must have at least one candy.
    Children with a higher rating get more candies than their neighbors.

Return the minimum number of candies you need to have to distribute the candies to the children.
"""
class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)

        for i, rating in enumerate(ratings):
            if i > 0:
                if ratings[i] > ratings[i - 1]:
                    if candies[i] <= candies[i - 1]:
                        candies[i] = candies[i - 1] + 1
            if i < len(ratings) - 1:
                if ratings[i] > ratings[i + 1]:
                    if candies[i] <= candies[i + 1]:
                        candies[i] = candies[i + 1] + 1

        for j, rating in enumerate(ratings):
            i = len(ratings) - 1 - j
            if i > 0:
                if ratings[i] > ratings[i - 1]:
                    if candies[i] <= candies[i - 1]:
                        candies[i] = candies[i - 1] + 1
            if i < len(ratings) - 1:
                if ratings[i] > ratings[i + 1]:
                    if candies[i] <= candies[i + 1]:
                        candies[i] = candies[i + 1] + 1

        print(candies)
        return sum(candies)
