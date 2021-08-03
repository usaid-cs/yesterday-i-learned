class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def product(items):
            start = 1
            for item in items:
                start = start * item
            return start
        
        array_l = [1]
        for idx, num in enumerate(nums[1:], start=1):
            array_l.append(array_l[idx - 1] * nums[idx - 1])
        # return array_l
        
        array_r = [1]
        for idx, num in reversed(list(enumerate(nums[:-1]))):
            array_r.insert(0, array_r[0] * nums[idx + 1])
        
        # print(array_l, array_r)
        return [x * y for x, y in zip(array_l, array_r)]
