class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        reversed_digits = reversed(digits)
        new_digits = []
        carry = 0
        for idx, digit in enumerate(reversed_digits):
            new_digit = digit + carry
            if idx == 0:
                new_digit += 1
            if new_digit >= 10:
                carry = 1
                new_digit -= 10
            else:
                carry = 0
            new_digits.append(new_digit)
        if carry:
            new_digits.append(1)
        return reversed(new_digits)
