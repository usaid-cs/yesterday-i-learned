class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        summ = 0
        answers = []
        for num in nums:
            summ = summ * 2 + num
            if summ % 5 == 0:
                answers.append(True)
            else:
                answers.append(False)
                summ = summ % 5
        return answers
