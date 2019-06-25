#!/usr/bin/env python3

import fnmatch
import os
import random
import re
from tempfile import mkstemp
from shutil import move
from optparse import OptionParser
from os import fdopen, remove

parser = OptionParser()
parser.add_option('--keyword', action='store', dest='keyword',
                  help='Reorganize only fun facts with a keyword.', default='')
(options, args) = parser.parse_args()
if args:
    parser.print_help()
    exit(1)


def get_item():
    items = []
    with open('random.md', 'r') as f:
        for line in f:
            if not (line.startswith('- ') or line.startswith('1.')):
                continue
            if not (not options.keyword or options.keyword in line.lower()):
                continue
            items.append(line.strip())
    if not items:
        return None
    line = random.choice(list(items))
    return line


def remove_item(pattern):
    file_path = 'random.md'
    #Create temp file
    fh, abs_path = mkstemp()
    with fdopen(fh, 'w') as new_file:
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
        if not line:
            print('There are no facts.')
            exit(1)

        print('\n' + line)
        new_file = input('Move to which file? Or (s)kip (d)elete e(x)it) ')
        if new_file == 's':
            continue
        elif new_file == 'x':
            return
        elif new_file == 'd':
            remove_item(line)
        elif len(new_file) > 1:
            if not new_file.endswith('.md'):
                new_file = new_file + '.md'
            if not os.path.isfile(new_file):
                print('Warning: {} does not exist; creating'.format(new_file))
            with open(new_file, 'a') as myfile:
                myfile.write(line + '\n')
            remove_item(line)


if __name__ == '__main__':
    # random.seed(0)
    main()
