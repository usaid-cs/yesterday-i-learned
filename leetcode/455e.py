class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # g is kids
        # s is cookies
        g.sort()
        s.sort()
        if not g:
            return 0
        if not s:
            return 0

        kids = 0
        while g:
            g_head = g.pop()
            for idx2, y in enumerate(s):
                if y >= g_head:
                    s.pop(idx2)
                    kids += 1
                    break

        return kids

