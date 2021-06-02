#!/bin/python3

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    builder = s
    while len(builder) < n:
        builder += s
    builder = builder[:n]
    return len([char for char in builder if char == 'a'])
