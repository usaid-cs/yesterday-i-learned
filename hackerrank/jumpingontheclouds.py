#!/bin/python3

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    """
    jumpingOnClouds has the following parameter(s):

    int c[n]: an array of binary integers

    Returns
    int: the minimum number of jumps required
    """
    if not c:
        return 0
    if len(c) <= 2:
        return 1  # Any solvable game with two clouds can only have a thunderhead at step 1
    steps = 0
    cur_idx = 0
    for idx, cloud in enumerate(c):
        if idx < cur_idx:
            continue
        try:
            hop = c[idx + 2]
            if hop == 0:
                cur_idx = idx + 2
                steps += 1
                continue
        except IndexError:
            pass
        assert not cloud, 'never expected to reach a thunderhead'
        try:
            c[idx + 1]
            cur_idx = idx + 1
            steps += 1
        except IndexError:
            pass
    return steps

assert jumpingOnClouds([0,1,0,0,0,1,0]) == 3
assert jumpingOnClouds([0,0,1,0,0,0,1,0]) == 4
assert jumpingOnClouds([0,0,0,0,1,0]) == 3
