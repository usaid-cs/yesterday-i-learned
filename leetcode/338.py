# (turns out the question didn't need your answer to be incredibly fast.)

from typing import List


def bits_in(num: int):
    return bin(num)[2:]


def ones_in(bits: List[str]):
    return len([x for x in bits if x == '1'])


class Solution:
    bit_cache = {}

    def countBits(self, num: int) -> List[int]:
        ret = []
        for x in range(num + 1):
            x_bits = bits_in(x)
            x_ones = ones_in(x_bits)
            self.bit_cache[x] = x_bits
            ret.append(x_ones)
        print(ret)
        return ret


a = Solution()
assert a.countBits(2) == [0, 1, 1]
assert a.countBits(5) == [0, 1, 1, 2, 1, 2]