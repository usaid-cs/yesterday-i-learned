class Solution:
    def isHappy(self, n: int) -> bool:
        def get_digits(num):
            digits = []
            while num:
                last_digit = num - (int(num // 10) * 10)
                digits.insert(0, last_digit)
                num = num // 10
            return digits

        def get_sum_of(digit_seq):
            return sum(digit * digit for digit in digit_seq)

        seen = set()
        while True:
            digits = get_digits(n)
            n = get_sum_of(digits)
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)
