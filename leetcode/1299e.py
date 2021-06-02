class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        largest = arr[-1]
        for idx, i in enumerate(reversed(arr)):
            if idx == 0:
                continue
            real_idx = length - idx - 1
            arr[real_idx] = max(arr[real_idx], arr[real_idx + 1])
            largest = arr[real_idx]
        arr.pop(0)
        arr.append(-1)
        return arr
