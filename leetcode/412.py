class Solution:
    def fizzBuzz(self, n: int):
        if not n:
            return []
        fuckall = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                fuckall.append("FizzBuzz")
            elif i % 3 == 0:
                fuckall.append("Fizz")
            elif i % 5 == 0:
                fuckall.append("Buzz")
            else:
                fuckall.append(str(i))
        return fuckall
