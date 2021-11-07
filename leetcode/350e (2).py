"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
"""
# oh you could have used a hashmap
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        common = []
        while nums1 and nums2:
            if nums1[0] == nums2[0]:
                common.append(nums1[0])
                nums1.pop(0)
                nums2.pop(0)
            elif nums1[0] > nums2[0]:
                nums2.pop(0)
            else:
                nums1.pop(0)
        return common