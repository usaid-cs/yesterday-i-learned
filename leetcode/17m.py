class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        chars = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        def recurse(rest_digits):
            if not rest_digits:
                return []
            if len(rest_digits) == 1:
                return chars[rest_digits[0]]

            combos = []
            rest_combos = recurse(rest_digits[1:])
            for char in chars[rest_digits[0]]:
                for combo in rest_combos:
                    combos.append(char + combo)
            return combos

        return recurse(digits)
