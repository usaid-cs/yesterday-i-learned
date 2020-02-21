from typing import List


class Solution:
    @staticmethod
    def frapp(lst):
        new_lst = [0] * len(lst)
        for idx, _ in enumerate(new_lst):
            new_lst[idx] = lst[idx]
            if idx != 0:
                new_lst[idx] += lst[idx - 1]
        new_lst.append(1)
        return new_lst

    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows:
            return []
        lst = [1]
        lsts = [lst]
        for _ in range(numRows - 1):
            lst = self.frapp(lst)
            lsts.append(lst)
        return lsts


a = Solution()
print(a.generate(0))
print(a.generate(1))
print(a.generate(2))
print(a.generate(3))
