class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        eh = {}
        for num in nums:
            if num in eh:
                return True
            eh[num] = 1
        return False