#!/bin/python3

def getSum(arr, y, x):
    return (
        arr[y][x] +
        arr[y-1][x-1] +
        arr[y-1][x] +
        arr[y-1][x+1] +
        arr[y+1][x-1] +
        arr[y+1][x] +
        arr[y+1][x+1])

# Complete the hourglassSum function below.
def hourglassSum(arr):
    max_sum = None
    # We know the hourglass matrix dimension can only be width(arr) - 2, height(arr) - 2
    for y, row in enumerate(arr):
        if y < 1 or y > len(arr) - 2:
            continue
        for x, cell in enumerate(row):
            if x < 1 or x > len(row) - 2:
                continue
            cell_sum = getSum(arr, y, x)
            if max_sum is None:
                max_sum = cell_sum
            else:
                max_sum = max(max_sum, cell_sum)
    return max_sum
