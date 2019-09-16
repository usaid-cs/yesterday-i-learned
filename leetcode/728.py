class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        nums = []
        for num in range(left, right + 1):
            if all(
                    int(digit) != 0 and num % int(digit) == 0
                    for digit in list(str(num))):
                nums.append(num)
        return nums