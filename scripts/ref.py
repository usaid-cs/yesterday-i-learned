#!/usr/bin/env python3

import fnmatch
import os
import random
import re
from tempfile import mkstemp
from shutil import move
from os import fdopen, remove


old_name = 'python.md'
new_name = 'python2.md'


def get_lines():
    with open(old_name, 'r') as f:
        return [line for line in f]


def get_links(lines):
    links = set()
    for line in lines:
        # looks like [('women have longer teeth than men', 'reddit 68'), ('a', 'b')]
        matches = re.findall(r'\[([^]]+)\]\(([^)]+)\)', line)
        if not matches:
            continue
        for (link_text, link_url) in matches:
            links.add(link_url)
    return list(links)


def main():
    lines = get_lines()
    links = get_links(lines)
    with open(new_name, 'w') as f:
        for line in lines:
            new_line = line
            for idx, link in enumerate(links):
                new_line = new_line.replace('](' + link + ')', '][' + str(idx) + ']')
            f.write(new_line)

        # At the bottom, write refs
        f.write('\n\n')
        for idx, link in enumerate(links):
            f.write('[%s]: %s\n' % (idx, link))


if __name__ == '__main__':
    main()
