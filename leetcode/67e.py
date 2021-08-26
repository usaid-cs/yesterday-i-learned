class Solution:
    def addBinary(self, a: str, b: str) -> str:
        buffer = ''
        carry = 0
        a_reversed, b_reversed = list(a[::-1]), list(b[::-1])
        while a_reversed or b_reversed:
            if a_reversed and b_reversed:
                a_first, b_first = a_reversed.pop(0), b_reversed.pop(0)
                total = int(a_first) + int(b_first) + carry
            elif a_reversed:
                a_first = a_reversed.pop(0)
                total = int(a_first) + carry
            elif b_reversed:
                b_first = b_reversed.pop(0)
                total = int(b_first) + carry
            if total == 3:
                total = 1
                carry = 1
            elif total == 2:
                total = 0
                carry = 1
            else:
                carry = 0
            buffer += str(total)
        if carry:
            buffer += '1'
        return buffer[::-1]
