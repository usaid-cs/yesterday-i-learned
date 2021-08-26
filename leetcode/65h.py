import re

class Solution:
    def isNumber(self, s: str) -> bool:
        integer = r'[+-]?\d+'
        decimal = r'[+-]?(\d+|\d+\.|\d*\.\d+)([eE][+-]?\d+)?'
        return bool(re.match(r'^(%s|%s)$' % (integer, decimal), s))
