class Solution:
    def isValid(self, s: str) -> bool:
        stek = []

        for char in s:
            if char == '(':
                stek.append(char)
            if char == '[':
                stek.append(char)
            if char == '{':
                stek.append(char)
            if char == ')':
                if (not stek) or stek.pop() != '(':
                    return False
            if char == ']':
                if (not stek) or stek.pop() != '[':
                    return False
            if char == '}':
                if (not stek) or stek.pop() != '{':
                    return False
        if stek:
            return False
        return True