# Complete the countSwaps function below.
def countSwaps(a):
    num_swaps = 0
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                num_swaps += 1
    print('Array is sorted in %d swaps.' % num_swaps)
    print('First Element: %s' % a[0])
    print('Last Element: %s' % a[-1])
