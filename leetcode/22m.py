# solution for cheaters
from itertools import permutations


def is_valid_string(parens):
    if not parens:
        return True
    if not parens.startswith('('):
        return False
    depth = 0
    for char in parens:
        if char == '(':
            depth += 1
        elif char == ')':
            depth -= 1
            if depth < 0:
                return False  # You can't do that
    return depth == 0


class Solution:
    def generateParenthesis(self, n: int):
        if n < 1:
            return []
        elif n == 1:
            return ['()']
        chars = '(' * n + ')' * n
        answers = set()
        for perm in permutations(chars):
            if perm.count('(') != n or perm.count(')') != n:
                continue
            if is_valid_string(perm):
                answers.add(perm)
        return list(answers)


truthy_cases = [
    '',
    '()',
    '(())',
    '()()',
    '()(()(()))',
]
for truthy_case in truthy_cases:
    assert is_valid_string(truthy_case) == True, truthy_case
falsy_cases = ['(', '())', '((())', '()()()((())']
for falsy_case in falsy_cases:
    assert is_valid_string(falsy_case) == False, falsy_case

# a = Solution()
# print(a.generateParenthesis(3))
for item in permutations('((()))'):
    print(''.join(item))
