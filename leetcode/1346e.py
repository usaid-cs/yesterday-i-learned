class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for idx, x in enumerate(arr):
            if x * 2 in arr:
                if arr.index(x * 2) != idx:
                    return True
        return False
