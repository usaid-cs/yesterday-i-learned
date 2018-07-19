#!/usr/bin/env python3

import fnmatch
import os
import random
import re
from tempfile import mkstemp
from shutil import move
from os import fdopen, remove


def get_item():
    items = []
    with open('random.md', 'r') as f:
        for line in f:
            if line.startswith('* ') or line.startswith('1.'):
                items.append(line.strip())
    line = random.choice(list(items))
    line = re.sub(r'^(\*|1\.)\s*', '', line)
    return line


def remove_item(pattern):
    file_path = 'random.md'
    #Create temp file
    fh, abs_path = mkstemp()
    with fdopen(fh,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                if pattern not in line:
                    new_file.write(line)
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)


def main():
    while True:
        # This reads the file over and over but oh well
        line = get_item()
        print(line)
        new_file = input('Move to which file? Or (s)kip e(x)it) ')
        if new_file == 's':
            continue
        elif new_file == 'x':
            return
        else:
            with open(new_file, 'a') as myfile:
                myfile.write(line)
            remove_item(line)


if __name__ == '__main__':
    main()
