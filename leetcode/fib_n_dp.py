def fib_n(n):
    cache = [None] * (n)
    cache[0] = 0
    cache[1] = 1
    for i in range(2, n):
        print(i, cache)
        cache[i] = cache[i - 1] + cache[i - 2]
    return cache[-1]


print(fib_n(6))
