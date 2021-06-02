class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        assert nums
        maxes = []
        for num in nums:
            if len(maxes) < 3:
                if num not in maxes:
                    maxes.append(num)
                continue
            max_of_maxes = max(maxes)
            min_of_maxes = min(maxes)
            if num > min_of_maxes:
                if num not in maxes:
                    maxes = [x for x in maxes if x != min_of_maxes] + [num]
        print(maxes)
        if len(maxes) >= 3:
            return sorted(maxes)[0]
        return max(maxes)
