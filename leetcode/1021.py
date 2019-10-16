class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        buffer = ''
        level = 0
        ls = []
        rs = []
        if not S:
            return S
        for current_char in S:
            if current_char == '(':
                if level == 0:
                    buffer += ''
                else:
                    buffer += current_char
                level += 1
            else:
                if level == 0:
                    raise ValueError('huh')
                else:
                    level -= 1
                    if level == 0:
                        buffer += ''
                    else:
                        buffer += current_char
        return buffer


a = Solution()
assert a.removeOuterParentheses('()') == ''
assert a.removeOuterParentheses('(())') == '()'
assert a.removeOuterParentheses('(()())(())') == '()()()'