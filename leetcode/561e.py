class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        lst1 = []
        lst2 = []
        while True:
            if nums:
                lst1.append(nums.pop(0))
            if nums:
                lst2.append(nums.pop(0))
            if not nums:
                break
        return sum(x for x in lst1)
