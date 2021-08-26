class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1

        counts = [(num, count) for (num, count) in counter.items()]
        counts.sort(key=lambda x: x[1], reverse=True)
        return [x for x, y in counts][:k]
