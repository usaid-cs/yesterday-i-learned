"""
Given a string expression of numbers and operators, return all possible
results from computing all the different possible ways to group numbers
and operators. You may return the answer in any order.
"""

import functools

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        symbols = ['+', '-', '*']

        @functools.cache
        def recurse(exp):
            if not any(symbol in exp for symbol in symbols):
                return [int(exp)]

            results = []
            for idx, char in enumerate(exp):
                if char in symbols:
                    left, right = exp[:idx], exp[idx + 1:]
                    for left_result in recurse(left):
                        for right_result in recurse(right):
                            if char == '+':
                                results.append(left_result + right_result)
                            elif char == '-':
                                results.append(left_result - right_result)
                            elif char == '*':
                                results.append(left_result * right_result)
            return results

        return recurse(expression)
