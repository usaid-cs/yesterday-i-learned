# This is the fucking fibonacci sequence
class Solution:
    def climbStairs(self, n: int) -> int:
        step_vals = [0, 1, 2]
        if n <= 2:
            return step_vals[n]

        while len(step_vals) <= n:
            cur_idx = len(step_vals)
            step_vals.append(step_vals[cur_idx - 1] + step_vals[cur_idx - 2])
        return step_vals[-1]


a = Solution()
assert a.climbStairs(0) == 0
assert a.climbStairs(1) == 1
assert a.climbStairs(2) == 2
assert a.climbStairs(3) == 3
assert a.climbStairs(4) == 5
assert a.climbStairs(5) == 8