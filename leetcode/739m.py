class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        fucking_stack = []

        # [73, 74, 75, 71, 69, 72, 76, 73]
        for current_idx, temp in enumerate(temperatures):
            while fucking_stack:
                top = fucking_stack[0]
                prev_temp = temperatures[top]
                if prev_temp >= temp:
                    break
                prev_idx = fucking_stack.pop(0)
                ans[prev_idx] = current_idx - prev_idx
            fucking_stack.insert(0, current_idx)
        return ans
