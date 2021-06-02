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

    def getRow(self, rowIndex: int) -> List[int]:
        if not rowIndex:
            return [1]
        lst = [1]
        for _ in range(rowIndex):
            lst = self.frapp(lst)
        return lst


a = Solution()
print(a.getRow(0))
print(a.getRow(1))
print(a.getRow(2))
print(a.getRow(3))
print(a.getRow(33))
