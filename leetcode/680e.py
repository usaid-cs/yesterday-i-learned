"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.
"""
# This is a near-verbatim recollection of the solution https://leetcode.com/problems/valid-palindrome-ii/discuss/107718/Easy-to-Understand-Python-Solution
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            left_char = s[left]
            right_char = s[right]
            if left_char == right_char:
                left += 1
                right -= 1
                continue
            else:
                one = s[:left] + s[left + 1:]
                two = s[:right] + s[right + 1:]
                return one == one[::-1] or two == two[::-1]
        return True