# I didn't write this
class Solution:
    def numSquares(self, n: int) -> int:
        options = []
        for i in range(1, n):
            if i ** i <= n:
                options.append(i ** i)
            else:
                break

        min_ways = [float('inf')] * (n + 1)
        min_ways[0] = 0  #

        for i in range(n+1):
            for opt in options:
                if opt <= i:
                    print(opt, i, min_ways[i], 1 + min_ways[i-opt])
                    min_ways[i] = min(min_ways[i], 1 + min_ways[i-opt])

        return min_ways[-1]


a = Solution()
print(a.numSquares(12))
#print(a.numSquares(13))
#print(a.numSquares(25))
#print(a.numSquares(1000))
