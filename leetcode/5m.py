# slow AF
palin_cache = {}

class Solution:
    def longestPalindrome(self, s: str) -> str:
        global palin_cache

        longest_palindrome = ''

        def is_palindrome(string):
            global palin_cache
            if string in palin_cache:
                return palin_cache[string]
            substring = string[1:-1]
            if substring in palin_cache:
                is_palin = palin_cache[substring] and string[0] == string[-1]
            else:
                is_palin = string == string[::-1]
            palin_cache[string] = is_palin
            return is_palin

        def recurse(idx):
            nonlocal longest_palindrome
            t = s[idx]
            assert is_palindrome(t)  # single-char palindrome
            left, right = idx, idx
            while left >= 0 and right <= len(s) - 1:
                for new_t in [
                    s[left:right],
                    s[left - 1:right],
                    s[left - 1:right + 1],
                    s[left:right + 1],
                ]:
                    if is_palindrome(new_t):
                        if len(new_t) > len(longest_palindrome):
                            longest_palindrome = new_t
                left -= 1
                right += 1

        for idx in range(len(s)):
            recurse(idx)
        return longest_palindrome
