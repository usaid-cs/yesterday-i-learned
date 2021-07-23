class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1
        max_count, max_el = 0, None
        for num, count in counter.items():
            if count >= max_count:
                max_count = count
                max_el = num
        return max_el
