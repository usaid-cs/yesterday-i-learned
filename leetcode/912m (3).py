class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def quicksort(arr, lo, hi):
            if lo < hi:
                index = partition(arr, lo, hi)
                quicksort(arr, lo, index - 1)
                quicksort(arr, index + 1, hi)
            return arr

        def partition(arr, lo, hi):
            i = lo
            pivot = arr[hi]
            for j in range(lo, hi):
                if arr[j] < pivot:
                    print('swapped %s with %s' % (arr[j], arr[i]))
                    arr[j], arr[i] = arr[i], arr[j]
                    i += 1
            print('then swapped %s with %s' % (arr[hi], arr[i]))
            arr[hi], arr[i] = arr[i], arr[hi]
            return i

        n = len(nums)
        if n <= 1:
            return nums
        return quicksort(nums, 0, n - 1)
