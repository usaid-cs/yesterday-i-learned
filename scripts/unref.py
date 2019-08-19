#!/usr/bin/env python3

import fnmatch
import os
import random
import re
from tempfile import mkstemp
from shutil import move
from os import fdopen, remove


old_name = 'python.md'
new_name = 'python.md'


def get_lines():
    with open(old_name, 'r') as f:
        return [line for line in f]


def get_link(lines, ref):
    matching_lines = [line for line in lines if line.startswith('[' + ref + ']:')]
    assert len(matching_lines) <= 1
    if not matching_lines:
        return None
    ref_line = matching_lines[0]
    link = re.findall(r':\s*(.+)$', ref_line)[0].strip()
    return link or None


def main():
    lines = get_lines()
    with open(new_name, 'w') as f:
        for line in lines:
            if line.startswith('[') and ']:' in line:
                continue

            # looks like [('women have longer teeth than men', 'reddit 68'), ('a', 'b')]
            ref_links = re.findall(r'\[([^]]+)\]\[([^]]+)\]', line)
            if not ref_links:
                f.write(line)
                continue

            for text, ref in ref_links:
                link = get_link(lines=lines, ref=ref)
                if not link:
                    print('Cant find link for', ref)
                    continue
                line = line.replace('][' + ref + ']', '](' + link + ')')
            f.write(line)


if __name__ == '__main__':
    main()
