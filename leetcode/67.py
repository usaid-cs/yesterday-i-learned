class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            b = '0' * (len(a) - len(b)) + b
        elif len(a) < len(b):
            a = '0' * (len(b) - len(a)) + a
        assert len(a) == len(b)
        carry = False
        buffer = ""
        for char_a, char_b in zip(reversed(a), reversed(b)):
            int_a = (char_a == '1')
            int_b = (char_b == '1')
            if not (int_a or int_b):
                if carry:
                    buffer = '1' + buffer
                else:
                    buffer = '0' + buffer
                carry = False
            elif (int_a and int_b):
                if carry:
                    buffer = '1' + buffer
                    # carry stays true
                else:
                    buffer = '0' + buffer
                carry = True
            else:
                if carry:
                    buffer = '0' + buffer
                else:
                    buffer = '1' + buffer
        if carry:
            buffer = '1' + buffer
        return buffer


a = Solution()
assert a.addBinary('0', '0') == '0'
assert a.addBinary('0', '1') == '1'
assert a.addBinary('1', '0') == '1'
assert a.addBinary('1', '1') == '10'
print(a.addBinary('11', '1'))
print(a.addBinary('11', '11'))