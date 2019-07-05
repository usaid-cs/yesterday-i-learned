class Solution:
    def duplicateZeros(self, arr) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        l = len(arr)
        i = 0
        while i < l:
            el = arr[i]
            if el == 0:
                arr.insert(i, 0)
                i += 2
            else:
                i += 1
        while len(arr) > l:
            del arr[-1]
