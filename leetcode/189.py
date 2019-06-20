class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        for _ in range(k):
            val = nums[-1]
            del nums[-1]
            nums.insert(0, val)