class Solution:
    def countAndSay(self, n: int) -> str:
        def get_prefix_count(some_str):
            assert some_str, 'what the hell man'
            lookup_char = some_str[0]
            count = 1
            for char in some_str[1:]:
                if char == lookup_char:
                    count += 1
                else:
                    break
            remainder = some_str[count:]
            if count >= 10:
                print(n)
            return lookup_char, count, remainder

        def recurse(num):
            if num == 1:
                return "1"
            previous_str = recurse(num - 1)
            new_str = ''
            while previous_str:
                lookup_char, count, previous_str = get_prefix_count(previous_str)
                new_str += '%s%s' % (count, lookup_char)
            return new_str
        
        return recurse(n)
    
    
a = Solution()
a.countAndSay(40)
