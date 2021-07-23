class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_list = []
        i = 0
        j = len(nums) - 1
        while i < j:  # [0 4] [1 3] [2 2]
            new_num_i = nums[i] * nums[i]
            new_num_j = nums[j] * nums[j]
            if new_num_i > new_num_j:
                new_list.insert(0, new_num_i)
                i += 1
            else:
                new_list.insert(0, new_num_j)
                j -= 1

        if i == j:
            new_list.insert(0, nums[i] ** 2)

        return new_list
