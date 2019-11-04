class Solution:
    def intToRoman(self, num: int) -> str:
        # print(num)
        assert 1 <= num <= 3999, 'wtf man'
        buffer = 'M' * int(num / 1000)
        num = num % 1000
        # print(num)
        if num >= 900:
            buffer += 'CM'
            num -= 900
        elif num >= 500:
            buffer += 'D' * int(num / 500)
            num = num % 500

        # print(num)
        if num >= 400:
            buffer += 'CD'
            num -= 400
        elif num >= 100:
            buffer += 'C' * int(num / 100)
            num = num % 100

        # print(num)
        if num >= 90:
            buffer += 'XC'
            num -= 90
        elif num >= 50:
            buffer += 'L' * int(num / 50)
            num = num % 50

        # print(num)
        if num >= 40:
            buffer += 'XL'
            num -= 40
        elif num >= 10:
            buffer += 'X' * int(num / 10)
            num = num % 10

        # print(num)
        if num >= 9:
            buffer += 'IX'
            num -= 9
        elif num >= 5:
            buffer += 'V' * int(num / 5)
            num = num % 5

        if num >= 4:
            buffer += 'IV'
            num = num % 4

        buffer += 'I' * int(num)
        return buffer


a = Solution()
assert a.intToRoman(3) == 'III'
assert a.intToRoman(499) == 'CDXCIX'
assert a.intToRoman(3999) == 'MMMCMXCIX'
assert a.intToRoman(144) == 'CXLIV', a.intToRoman(144)
assert a.intToRoman(2014) == 'MMXIV'
assert a.intToRoman(3049) == 'MMMXLIX'