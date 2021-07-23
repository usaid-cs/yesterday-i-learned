class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        assert strs, 'yo man dont do this to me'
        current_counter = ''
        while sum(len(s) for s in strs):
            first_string = strs[0]
            for idx, string in enumerate(strs[1:]):
                # In case either string is empty
                if not (string and first_string):
                    return current_counter
                if string[0] != first_string[0]:
                    return current_counter
                else:
                    strs[idx + 1] = strs[idx + 1][1:]
            current_counter += first_string[0]
            strs[0] = strs[0][1:]
        return current_counter
