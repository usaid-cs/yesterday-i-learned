from collections import defaultdict

# They say use a sliding window for O(n) but my sliding window is the bottom 5%
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        c = defaultdict(int)

        def get_letters():
            return {letter for letter in c if c[letter] > 0}

        left = 0
        right = 1
        longest = 1
        c[s[left]] += 1
        right_visited = set()

        while left < len(s) - 1:
            if right not in right_visited:
                new_char = s[right]
                c[new_char] += 1
                right_visited.add(right)
            letters = get_letters()
            if len(letters) > 2:
                c[s[left]] -= 1
                left += 1
                if right < left:
                    right = left
                continue
            else:
                # print(right, left)
                longest = max(longest, right - left + 1)
                if right < len(s) - 1:
                    right += 1
                else:
                    break
        return longest