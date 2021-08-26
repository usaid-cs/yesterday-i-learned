class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palin = s[0]

        def expand_around(left, right):
            if not (left >= 0 and right <= len(s) - 1):
                return left, left
            if s[left] != s[right]:
                return left, left
            while True:
                if left > 0 and right < len(s) - 1:
                    if s[left - 1] == s[right + 1]:
                        left -= 1
                        right += 1
                    else:
                        break
                else:
                    break
            return left, right

        left, right = 0, 0
        for idx in range(len(s)):
            expanded_left, expanded_right = expand_around(idx, idx)
            if expanded_right - expanded_left > right - left:
                right, left = expanded_right, expanded_left
                print(s, 1, left, right)
                longest_palin = s[left:right + 1]
            expanded_left, expanded_right = expand_around(idx, idx + 1)
            if expanded_right - expanded_left > right - left:
                right, left = expanded_right, expanded_left
                print(s, 2, left, right)
                longest_palin = s[left:right + 1]
        return longest_palin
