class Solution:
    def bitwiseComplement(self, N: int) -> int:
        b = bin(N)
        b = ['1' if x == '0' else '0' for x in b[2:]]
        b = ''.join(b).lstrip('0')
        if not b:
            return 0
        return int('0b' + b, 2)