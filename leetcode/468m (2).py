class Solution:
    def validIPAddress(self, IP: str) -> str:
        def is_valid_ipv4(test_str):
            if not test_str:
                return False
            parts = test_str.split('.')
            if len(parts) != 4:
                return False
            for part in parts:
                try:
                    part_int = int(part)
                except:
                    return False
                if len(part) != len(str(part_int)):
                    return False
                if not (0 <= part_int <= 255):
                    return False
            return True

        def is_valid_ipv6(test_str):
            ipv6_charset = set(['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f'])
            if not test_str:
                return False
            parts = test_str.split(':')
            if len(parts) != 8:
                return False
            for part in parts:
                part = part.lower()
                if not (1 <= len(part) <= 4):
                    return False
                if set([char for char in part]) - ipv6_charset:
                    return False
            return True

        if is_valid_ipv4(IP):
            return "IPv4"
        if is_valid_ipv6(IP):
            return "IPv6"
        return "Neither"
