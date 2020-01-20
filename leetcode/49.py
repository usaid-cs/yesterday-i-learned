from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        res = defaultdict(list)
        for string in strs:
            key = tuple(sorted(string))
            res[key].append(string)
        return list(res.values())


a = Solution()
print(a.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))