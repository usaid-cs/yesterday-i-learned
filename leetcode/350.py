from typing import List

# "elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once"


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        intersection = []
        for num in nums1:
            if num in nums2:
                intersection.append(num)
                # Relies on .remove() removing the first occurrence instead of any other one
                nums2.remove(num)
        return intersection