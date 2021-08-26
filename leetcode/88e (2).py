class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            # Remove spaces
            nums1.pop()
        idx = 0
        while nums2:
            first_num2 = nums2.pop(0)
            print(nums1, len(nums1))
            while idx < len(nums1):
                if first_num2 <= nums1[idx]:
                    nums1.insert(idx, first_num2)
                    break
                idx += 1
            else:
                nums1.insert(idx, first_num2)
