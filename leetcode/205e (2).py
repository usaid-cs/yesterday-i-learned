class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for s_char, t_char in zip(s, t):
            s_dict[s_char] = t_char
            t_dict[t_char] = s_char

        new_s = ''
        for s_char in s:
            new_s += s_dict[s_char]

        new_t = ''
        for t_char in t:
            new_t += t_dict[t_char]

        return t == new_s and s == new_t
