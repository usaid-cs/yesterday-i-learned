class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        total = 0
        exp = 0
        while num1 or num2:
            if num1:
                num1, last_digit1 = num1[:-1], int(num1[-1])
            else:
                num1, last_digit1 = "", 0
            if num2:
                num2, last_digit2 = num2[:-1], int(num2[-1])
            else:
                num2, last_digit2 = "", 0
            total += ((last_digit1 + last_digit2 + carry) % 10) * (10 ** exp)
            if last_digit1 + last_digit2 + carry > 9:
                carry = 1
            else:
                carry = 0
            exp += 1
        if carry:
            total += 10 ** exp
        return str(total)
