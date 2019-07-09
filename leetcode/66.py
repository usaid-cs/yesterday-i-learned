from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return digits

        carry = False
        digits[-1] += 1
        for idx in reversed(range(len(digits))):
            digit = digits[idx]
            if carry:
                digit += 1
            carry = digit >= 10  # == will do really
            digits[idx] = digit % 10

        if carry:  # Leftmost digit was a 9
            digits.insert(0, 1)
        print(digits)
        return digits


a = Solution()
assert a.plusOne([1, 2, 3]) == [1, 2, 4]
assert a.plusOne([9]) == [1, 0]
assert a.plusOne([9, 9]) == [1, 0, 0]