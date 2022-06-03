class Solution:
    def minimumSum(self, num: int) -> int:
        strn = str(num)

        def add(str1, str2):
            return int(str1) + int(str2)

        strl = sorted(strn)
        new1 = strl[0] + strl[2]
        new2 = strl[1] + strl[3]

        return add(new1, new2)
