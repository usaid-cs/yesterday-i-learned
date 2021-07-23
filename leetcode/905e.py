class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even_buffer = []
        odd_buffer = []
        i = 0
        while nums:
            item = nums[i]
            if item % 2 == 0:
                even_buffer.append(item)
            else:
                odd_buffer.append(item)
            nums.pop(0)
        for item in even_buffer:
            nums.append(item)
        for item in odd_buffer:
            nums.append(item)
        return nums
