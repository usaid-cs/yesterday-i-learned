class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the pivot point

        new_start = 0
        searches = [(0, len(nums) - 1)]
        while searches:
            left, right = searches.pop(0)
            if left > right:
                continue
            middle = (left + right) // 2
            if middle > 0 and nums[middle - 1] > nums[middle]:
                new_start = middle
                break
            else:
                searches.append((left, middle - 1))
                searches.append((middle + 1, right))

        # pivot the damn thing
        new_nums = nums[new_start:] + nums[:new_start]

        # search in sorted list
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if new_nums[middle] == target:
                return (middle + new_start) % len(nums)
            elif new_nums[middle] < target:
                left = middle + 1
            elif new_nums[middle] > target:
                right = middle - 1
        return -1
