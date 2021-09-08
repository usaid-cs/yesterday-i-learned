# Hashing a string into a binary representation helps compare them in linear time, and storing the max length for each
# binary representation in a hashmap is just icing on the cake
class Solution:
    def maxProduct(self, words: List[str]) -> int:

        def string_to_bool(string):
            mask = 0b0
            for ord_of in range(ord('a'), ord('z') + 1):
                char = chr(ord_of)
                offset = ord_of - ord('a')
                if char in string:
                    mask ^= (0b1 << offset)
            return mask

        word_map = {}
        for string in words:
            bin_ = string_to_bool(string)
            if bin_ in word_map:
                word_map[bin_] = max(word_map[bin_], len(string))
            else:
                word_map[bin_] = len(string)

        max_len = 0
        for bin1, len1 in word_map.items():
            for bin2, len2 in word_map.items():
                if bin1 & bin2 == 0b0:
                    max_len = max(max_len, len1 * len2)
        return max_len
