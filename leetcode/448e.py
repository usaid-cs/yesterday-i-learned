class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        max_num = len(nums)
        nums.sort()
        print(nums)

        missing = []
        for i in range(1, max_num + 1):
            if nums and nums[0] == i:
                while nums and nums[0] == i:
                    nums.pop(0)
            else:
                missing.append(i)
        return missing
