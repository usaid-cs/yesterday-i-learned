class Solution:
    def countAndSay(self, n: int) -> str:
        def str_to_say(number_str):
            if not number_str:
                raise NotImplementedError('wtf')
            if len(number_str) == 1:
                return '1' + number_str
            buffer = ''
            current_number = number_str[0]
            current_count = 1
            idx = 1
            while idx < len(number_str):
                substr = number_str[idx]
                if substr == current_number:
                    current_count += 1
                    idx += 1
                else:
                    buffer += str(current_count) + current_number
                    current_number = substr
                    current_count = 1
                    idx += 1
            buffer += str(current_count) + current_number
            return buffer

        lol = '1'
        for _ in range(n - 1):
            lol = str_to_say(lol)
        return lol