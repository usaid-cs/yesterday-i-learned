class Solution:
    def balancedStringSplit(self, s: str) -> int:
        if not s:
            return 0
        pops = {
            'L': [],
            'R': [],
        }
        groups = 0
        while s:
            current_char, s = s[0], s[1:]
            pops[current_char].append(current_char)
            if len(pops['L']) == len(pops['R']):
                pops['L'] = []
                pops['R'] = []
                groups += 1
        return groups


a = Solution()
print(a.balancedStringSplit('LLLLRRRR'))  # 1
print(a.balancedStringSplit('RLRRLLRLRL'))  # 4
print(a.balancedStringSplit('RLLLLRRRLR'))  # 3