class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) <= 1:
            return 1
        chars = list(s)
        single_chars = [char for char in set(chars) if chars.count(char) == 1]
        odd_chars = [
            char for char in set(chars)
            if chars.count(char) % 2 and chars.count(char) != 1
        ]
        odd_chars.sort(key=lambda char: (-chars.count(char), char))
        even_chars = [
            char for char in set(chars) if chars.count(char) % 2 == 0
        ]
        even_chars.sort(key=lambda char: (-chars.count(char), char))

        max_len = 0
        if single_chars:
            max_len += 1
        odd_chars_len = sum(chars.count(char) - 1 for char in odd_chars)
        max_len += odd_chars_len
        even_chars_len = sum(chars.count(char) for char in even_chars)
        max_len += even_chars_len
        if not single_chars and odd_chars:
            max_len += 1
        return max_len


a = Solution()
assert a.longestPalindrome('ccc') == 3
assert a.longestPalindrome('abccccdd') == 7
assert a.longestPalindrome(
    'Givenastringwhichconsistsoflowercaseoruppercaselettersfindthelengthofthelongestpalindromesthatcanbebuiltwiththoseletters'
) == 109
