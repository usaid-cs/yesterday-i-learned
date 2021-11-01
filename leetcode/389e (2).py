class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = [_ for _ in s]
        t = [_ for _ in t]
        s.sort()
        t.sort()
        while s and t:
            s_first = s.pop(0)
            t_first = t.pop(0)
            if s_first != t_first:
                return t_first
        return t[0]
