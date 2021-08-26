class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        chars1 = {}
        for num in nums1:
            if num in chars1:
                chars1[num] += 1
            else:
                chars1[num] = 1

        chars2 = {}
        for num in nums2:
            if num in chars2:
                chars2[num] += 1
            else:
                chars2[num] = 1

        common_keys = set(x for x in nums1 + nums2 if x in nums1 and x in nums2)
        output = []
        for common_key in common_keys:
            occurrences = min(chars1[common_key], chars2[common_key])
            output.extend([common_key] * occurrences)
        return output
