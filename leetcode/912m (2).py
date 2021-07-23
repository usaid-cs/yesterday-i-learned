class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge_sort(arr):
            n = len(arr)
            if n <= 1:
                return arr
            left, right = merge_sort(arr[:n // 2]), merge_sort(arr[n // 2:])  # one could to be longer than another

            return merge(left, right)

        def merge(left, right):
            buffer = []
            while left or right:
                if left and right:
                    left_head = left[0]
                    right_head = right[0]
                    if left_head <= right_head:
                        buffer.append(left_head)
                        left.pop(0)
                    else:
                        buffer.append(right_head)
                        right.pop(0)
                elif left:
                    buffer.append(left.pop(0))
                elif right:
                    buffer.append(right.pop(0))
            return buffer

        return merge_sort(nums)
