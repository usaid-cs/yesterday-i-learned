from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int],
              n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx1 = 0
        while nums2:
            num1 = nums1[idx1]
            num2 = nums2[0]
            if num2 >= num1:
                idx1 += 1
                if idx1 >= m:
                    break
            else:
                nums1.insert(idx1, num2)
                nums1.pop(-1)
                nums2.pop(0)
        if nums2:
            while nums2:
                num2 = nums2.pop(0)
                nums1.insert(idx1, num2)
                nums1.pop(-1)
                idx1 += 1


a = Solution()
arr = [4, 5, 6, 0, 0, 0]
a.merge(arr, 3, [1, 2, 3], 3)
print(arr)

arr = [1, 2, 3, 0, 0, 0]
a.merge(arr, 3, [4, 5, 6], 3)
print(arr)

arr = [1, 3, 5, 0, 0, 0]
a.merge(arr, 3, [2, 4, 6], 3)
print(arr)