# You are supposed to use binary manipulation.
import re

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        n_bin = bin(n)[2:]
        return bool(re.match('^10*$', n_bin))