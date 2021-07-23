def validate_ipv4(ip):
    if not all(chr in '0123456789.' for chr in ip):
        return False
    sections = ip.split('.')
    if len(sections) != 4:
        return False
    for section in sections:
        if section != '0' and section.startswith('0'):
            return False
        try:
            section_val = int(section)
        except (ValueError, TypeError):
            # bullshit in the value
            return False
        if not 0 <= section_val <= 255:
            return False
    return True


def is_good_section(section):
    if not section:
        return False
    if len(section) > 4:
        return False
    if not all(chr.upper() in '0123456789ABCDEF' for chr in section):
        return False
    return True


def validate_ipv6(ip):
    sections = ip.split(':')
    if len(sections) != 8:
        return False
    # I was told the groups are never completely collapsed into ::
    return all(is_good_section(section) for section in sections)


class Solution:
    def validIPAddress(self, IP: str) -> str:
        if not IP:
            return 'Neither'
        if '.' not in IP and ':' not in IP:
            return 'Neither'
        if '.' in IP:
            return 'IPv4' if validate_ipv4(IP) else 'Neither'
        return 'IPv6' if validate_ipv6(IP) else 'Neither'