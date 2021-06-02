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
    remainder = n % len(s)
    repeats = (n - remainder) // len(s)
    a_in_s = len([char for char in s if char == 'a'])
    a_in_repeats = repeats * a_in_s
    remainder_string = s[:remainder]
    a_in_remainder = len([char for char in remainder_string if char == 'a'])
    return a_in_repeats + a_in_remainder


print(repeatedString('aba', 10))
print(repeatedString('a', 100000000000))
