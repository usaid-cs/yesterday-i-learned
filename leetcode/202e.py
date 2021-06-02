class Solution:
    def isHappy(self, n: int) -> bool:
        def happy(num):
            digits = [char for char in str(num)]
            squares = [int(n) * int(n) for n in digits]
            return sum(squares)

        num = n
        visited = set()
        while True:
            output = happy(num)
            print(num, output)
            if output == 1:
                return True
            if len(str(output)) == 1 and output in visited:
                return False
            visited.add(output)
            num = output
