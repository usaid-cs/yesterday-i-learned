class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        buffer_s = ''
        for char in s:
            if char == '#':
                buffer_s = buffer_s[:-1]
            else:
                buffer_s += char

        buffer_t = ''
        for char in t:
            if char == '#':
                buffer_t = buffer_t[:-1]
            else:
                buffer_t += char

        return buffer_s == buffer_t
