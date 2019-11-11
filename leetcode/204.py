rubbish = set()
rubbish_max = 0
primes = set()


def is_prime(number):
    global rubbish_max
    if number in [0, 1]:
        return False
    if number in primes:
        return True
    if number in rubbish:
        return False
    # sqrt_ed = int(number**0.5) + 1
    for test in range(2, number):
        if number in rubbish:
            continue
        if number % test != 0:
            continue
        # test itself might still be a prime though
        rubbish.add(number)
        return False
    primes.add(number)
    return True


class Solution:
    def countPrimes(self, n: int) -> int:
        prime_count = 0
        sqrt_ed = int(n**0.6) + 1
        for num in range(2, sqrt_ed):
            if is_prime(num):
                prime_count += 1

        return prime_count


test_cases = [
    (0, 0),
    (1, 0),
    (2, 0),
    (3, 1),
    (4, 2),
    (5, 2),
    (6, 3),
    (7, 3),
    (8, 4),
    (9, 4),
    (10, 4),
    (99999, 9592),
    (999983, 78497),
]
a = Solution()
for n, expected in test_cases:
    output = a.countPrimes(n)
    print(n)
    assert output == expected, (n, expected, output)
