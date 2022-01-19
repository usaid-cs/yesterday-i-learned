import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();

        for (char c : s.toCharArray()) {
            if (isOpen(c)) {
                stack.add(c);
            } else if (isClose(c)) {
                // can't peek unless i check if it's empty first, are you fucking serious
                if (stack.isEmpty()) {
                    return false;
                }
                char d = stack.peek();
                if (getComplement(d) == c) {
                    stack.pop();
                } else {
                    return false;
                }
            }
        }

        return stack.isEmpty();
    }

    public boolean isOpen(char c) {
        return c == '(' || c == '{' || c == '[';
    }

    public boolean isClose(char c) {
        return c == ')' || c == '}' || c == ']';
    }

    public char getComplement(char c) {
        if (c == '(') {
            return ')';
        } else if (c == '[') {
            return ']';
        } else if (c == '{') {
            return '}';
        }
        return '_';
    }
}
