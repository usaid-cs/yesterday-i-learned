# Doing it this way just because it's a practice for the two-pointer technique
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        head = 0
        tail = len(nums) - 1
        removed = 0
        while head <= tail:
            num = nums[head]
            if num == val:
                nums[head], nums[tail] = nums[tail], nums[head]
                nums[tail]
                removed += 1
                tail -= 1
            else:
                head += 1
        for _ in range(removed):
            nums.pop()
