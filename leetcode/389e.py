class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        assert len(s) < len(t), 'wtf that wasnt the deal'
        chars = list(sorted(list(s)))
        chart = list(sorted(list(t)))

        while chars and chart:
            char_s = chars.pop(0)
            char_t = chart.pop(0)
            if char_s != char_t:
                return char_t
        return chart[0]


a = Solution()
assert a.findTheDifference('abcd', 'abcde') == 'e'
assert a.findTheDifference('a', 'aa') == 'a'