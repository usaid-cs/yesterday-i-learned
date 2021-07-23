class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for t in s:
            if t in ['(', '[', '{']:
                stack.insert(0, t)
                continue
            if not stack:
                return False  # no matching bracket
            if t == ')':
                top = stack.pop(0)
                if top != '(':
                    return False
            elif t == ']':
                top = stack.pop(0)
                if top != '[':
                    return False
            elif t == '}':
                top = stack.pop(0)
                if top != '{':
                    return False
        return not stack
