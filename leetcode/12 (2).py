class Solution:
    def intToRoman(self, num: int) -> str:
        buffer = ""
        while num >= 1000:
            buffer += "M"
            num -= 1000
        if 999 >= num >= 900:
            buffer += "CM"
            num -= 900
        if 900 > num >= 500:
            buffer += "D"
            num -= 500
        if 500 > num >= 400:
            buffer += "CD"
            num -= 400

        while num >= 100:
            buffer += "C"
            num -= 100
        if 99 >= num >= 90:
            buffer += "XC"
            num -= 90
        if 90 > num >= 50:
            buffer += "L"
            num -= 50
        if 50 > num >= 40:
            buffer += "XL"
            num -= 40

        while num >= 10:
            buffer += "X"
            num -= 10
        if num == 9:
            buffer += "IX"
            num -= 9
        if 90 > num >= 50:
            buffer += "V"
            num -= 5

        while num >= 5:
            buffer += "V"
            num -= 5
        if num == 4:
            buffer += 'IV'
            num -= 4

        buffer += num * 'I'
        return buffer
