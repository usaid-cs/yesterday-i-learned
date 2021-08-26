class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        counter = set()
        for idx, num in enumerate(nums):
            if num in counter:
                return True

            # This is how you keep a sliding window of at most length k
            counter.add(num)
            if len(counter) > k:
                counter.remove(nums[idx - k])
        return False
