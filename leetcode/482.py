def break_string_into_parts(s, l=1):
    buffer = ''
    for char in reversed(s):
        buffer += char
        if len(buffer) >= l:
            yield buffer[::-1]
            buffer = ''
    yield buffer[::-1]


class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.upper().replace('-', '')
        buffer = [str(x) for x in break_string_into_parts(S, K)]
        buffer = [x for x in buffer if x]
        return '-'.join(reversed(buffer))