class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones_dict = {}
        for stone in stones:
            if stone in stones_dict:
                stones_dict[stone] += 1
            else:
                stones_dict[stone] = 1

        is_jewel = 0
        for jewel in jewels:
            if jewel in stones_dict:
                is_jewel += stones_dict[jewel]
                stones_dict[jewel] = 0
        return is_jewel
