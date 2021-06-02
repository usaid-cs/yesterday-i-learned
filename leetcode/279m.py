class Solution:
    def numSquares(self, n: int) -> int:
        squares_to_use = []
        for i in range(1, n + 1):
            if i * i <= n:
                squares_to_use.append(i * i)
            else:
                break

        if n in squares_to_use:
            return 1

        tried_solns = set()
        solns = []
        for square_to_use in squares_to_use:
            solns.append((square_to_use,))
        while solns:
            soln = solns.pop(0)
            formula = sum(soln)
            tried_solns.add(soln)
            if formula > n:
                continue
            if formula == n:
                return len(soln)
            for square_to_use in reversed(squares_to_use):
                new_soln = soln + (square_to_use,)
                if new_soln not in tried_solns:
                    solns.append(new_soln)
