class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        def dec2bin(num):
            return bin(num)[2:]

        def count_bits(bin_num):
            return len([x for x in bin_num if x == '1'])

        def is_prime(num):
            if num == 1:
                return False
            if num in [2, 3, 5, 7]:
                return True
            for i in range(2, num):
                if (num / i) % 1 == 0:
                    return False
            return True

        def bits_set_is_prime(num):
            is_it = is_prime(count_bits(dec2bin(num)))
            return is_it

        return len([i for i in range(L, R + 1) if bits_set_is_prime(i)])


a = Solution()
assert a.countPrimeSetBits(6, 10) == 4
assert a.countPrimeSetBits(10, 15) == 5