class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        total = 0
        nums = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
        }
        for index1, char1 in enumerate(reversed(num1)):
            for index2, char2 in enumerate(reversed(num2)):
                digit1 = nums[char1]
                digit2 = nums[char2]
                total += digit1 * digit2 * pow(10, index1) * pow(10, index2)
        reverse_nums = {
            v: k for k, v in nums.items()
        }
        str_buffer = ""
        print(total)
        while total:
            last_digit = total - (total // 10 * 10)
            total -= last_digit
            total = total // 10
            str_buffer = reverse_nums[last_digit] + str_buffer
        return str_buffer
