# It's supposed to be hard, so I might be missing something here, but everyone else is doing it this way so I don't know man

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        nums_total = sorted(nums1 + nums2)
        len_total = len1 + len2
        if len_total % 2 == 0:
            return (nums_total[len_total // 2 - 1] + nums_total[len_total // 2]) / 2
        elif len_total % 2 == 1:
            return nums_total[len_total // 2]
        else:
            assert False
