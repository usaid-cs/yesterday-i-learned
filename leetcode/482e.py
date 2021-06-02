class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '')
        buffer = ''
        while s:
            s, taken = s[:-k], s[-k:]
            buffer = taken + '-' + buffer
        buffer = buffer.strip('-')
        return buffer.upper()
