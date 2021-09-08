class Solution:
    def countLargestGroup(self, n: int) -> int:
        def get_digit_sum(num):
            return sum([int(x) for x in str(num)])

        counter = {}
        for i in range(1, n + 1):
            digit_sum = get_digit_sum(i)
            if digit_sum in counter:
                counter[digit_sum].append(i)
            else:
                counter[digit_sum] = [i]

        max_nums = 0
        for sum_, nums in counter.items():
            if len(nums) > max_nums:
                max_nums = len(nums)

        num_groups = 0
        for sum_, nums in counter.items():
            if len(nums) == max_nums:
                num_groups += 1
        return num_groups
