class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip(' ')
        if not s:
            return 0
        if not any(s.startswith(x) for x in '+-0123456789'):
            return 0
        firstchar = s[0]
        if firstchar == '-':
            negative = True
            val, s = 0, s[1:]
        elif firstchar == '+':
            negative = False
            val, s = 0, s[1:]
        else:
            negative = False
            val, s = 0, s

        for char in s:
            if char not in '0123456789':
                break
            val += int(char)
            val *= 10
        val /= 10

        if negative:
            val = -val
        if val > 2147483647:
            return 2147483647
        if val < -2147483648:
            return -2147483648
        return int(val)


a = Solution()
maps = [
    ('+1', 1),
    ('42', 42),
    ('-42', -42),
    ('4193 with words', 4193),
    (' -4193 with words', -4193),
    ('words and 987', 0),
    ('-91283472332', -2147483648),
]
for s, v in maps:
    assert a.myAtoi(s) == v, (s, a.myAtoi(s))