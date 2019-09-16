from typing import List


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        strings = ['']
        S = S.lower()
        for s in S:
            if s.isalpha():
                for idx in range(len(strings)):
                    m = strings[idx]
                    strings[idx] += s.lower()
                    strings.append(m + s.upper())
            else:
                for idx in range(len(strings)):
                    strings[idx] += s.lower()
        return strings


a = Solution()
print(a.letterCasePermutation('a1b2'))
print(a.letterCasePermutation("3z4"))