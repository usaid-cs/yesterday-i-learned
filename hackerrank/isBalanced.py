def isBalanced(s):
    # Write your code here
    stack = []
    for char in s:
        if char in ('[', '(', '{'):
            stack.insert(0, char)
        elif char == ']':
            if (not stack) or stack[0] != '[':
                return 'NO'
            stack.pop(0)
        elif char == ')':
            if (not stack) or stack[0] != '(':
                return 'NO'
            stack.pop(0)
        elif char == '}':
            if (not stack) or stack[0] != '{':
                return 'NO'
            stack.pop(0)
    if stack:
        return 'NO'
    return 'YES'


print(isBalanced('}][}}(}][))]'))

print(isBalanced('[](){()}'))

print(isBalanced('()'))

print(isBalanced('({}([][]))[]()'))

print(isBalanced('{)[](}]}]}))}(())('))

print(isBalanced('([[)'))
