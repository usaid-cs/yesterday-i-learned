#!/bin/python3

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    if steps == 0:
        return 0
    valleys = 0
    level = 0
    in_valley = False
    for step in path:
        if step == 'U':
            level += 1
            if level >= 0 and in_valley == True:
                in_valley = False
        elif step == 'D':
            level -= 1
            if level < 0 and in_valley == False:
                in_valley = True
                valleys += 1
    return valleys



assert countingValleys(8, 'DDUUUUDD') == 1
assert countingValleys(2, 'UU') == 0
assert countingValleys(4, 'DDUU') == 1
assert countingValleys(8, 'DDUUDDUU') == 2
assert countingValleys(12, 'DDUUUUDDDDUU') == 2
