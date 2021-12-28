import functools


class Solution:
    def longestPalindrome(self, s: str) -> str:

        @functools.lru_cache(maxsize=None)
        def is_palin(substring):
            if len(substring) <= 1:
                return True
            if substring[0] != substring[-1]:
                return False
            return is_palin(substring[1:-1])

        if len(s) <= 1:
            return s

        max_substr = ''
        for idx, char in enumerate(s):
            left = right = idx
            # Odd strings
            while is_palin(s[left:right + 1]) and left >= 0 and right <= len(s) - 1:
                if len(s[left:right + 1]) > len(max_substr):
                    max_substr = s[left:right + 1]
                left -= 1
                right += 1
            # Even strings
            left = right = idx
            while is_palin(s[left - 1:right + 1]) and left >= 0 and right <= len(s) - 1:
                if len(s[left - 1:right + 1]) > len(max_substr):
                    max_substr = s[left - 1:right + 1]
                left -= 1
                right += 1
        return max_substr