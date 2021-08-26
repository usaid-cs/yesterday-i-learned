class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def get_raw(string):
            return tuple(sorted(list(string)))

        anagrams = {}
        for string in strs:
            raw = get_raw(string)
            if raw in anagrams:
                anagrams[raw].append(string)
            else:
                anagrams[raw] = [string]
        return list(anagrams.values())
