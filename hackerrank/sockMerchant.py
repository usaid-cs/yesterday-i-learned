#!/bin/python3

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    """
    sockMerchant has the following parameter(s):

    int n: the number of socks in the pile
    int ar[n]: the colors of each sock

    Returns

    int: the number of pairs
    """
    colors = {}
    socks = ar
    for sock in socks:
        if sock in colors:
            colors[sock] += 1
        else:
            colors[sock] = 1
    pairs = 0
    for k in colors.values():
        pairs += (k - k % 2) // 2
    return pairs


assert sockMerchant(0, [10,20,20,10,10,30,50,10,20]) == 3
