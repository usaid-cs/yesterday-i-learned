class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def string_to_sequence(string):
            assert string
            base = ord(string[0])
            buffer = [0]
            for char in string[1:]:
                offset = ord(char) - base
                if offset < 0:
                    offset += 26
                buffer.append(offset)
            return buffer

        dct = {}
        for string in strings:
            offsets = tuple(string_to_sequence(string))
            if offsets in dct:
                dct[offsets].append(string)
            else:
                dct[offsets] = [string]
        return [x for x in dct.values()]
