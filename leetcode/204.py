#!/usr/bin/env python3.6
# coding=utf-8


def thing(n):
    prime_map = {
        0: False,
        1: False,
    }

    def is_prime(n_):
        try:
            return prime_map[n_]
        except KeyError:
            pass
        for prime, is_prime_ in prime_map.items():
            if prime in [0, 1]:
                continue
            if n_ % prime == 0:
                prime_map[n_] = False
                return False
        prime_map[n_] = True
        return True

    for num in range(n):
        is_prime(num)

    return len([q for q in prime_map.values() if q])


test_cases = [
    (0, 0),
    (1, 0),
    (2, 0),
    (3, 1),
    (4, 2),
    (5, 2),
    (499979, 0),
]

for input_, expected in test_cases:
    assert thing(input_) == expected, (input_, expected, thing(input_))
