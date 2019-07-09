class Solution:
    def reverse(self, x: int) -> int:
        min_int = -2**31
        max_int = 2**31 - 1
        positive = x >= 0
        x = abs(x)
        buffer = 0
        while x:
            last_digit = x % 10
            buffer *= 10
            buffer = buffer + last_digit
            x = int(x / 10)

        if not positive:
            buffer = -buffer
        if not min_int <= buffer <= max_int:
            return 0
        return buffer