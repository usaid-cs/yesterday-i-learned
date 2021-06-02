class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def hash_func(string):
            dc = {}
            counter = 0
            buffer = ''
            for char in string:
                if char not in dc:
                    dc[char] = counter
                    counter += 1
                buffer += str(dc[char])
            return buffer

        return hash_func(s) == hash_func(t)
