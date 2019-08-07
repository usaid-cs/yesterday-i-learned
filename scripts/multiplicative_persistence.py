import operator
from functools import reduce


# Mod of https://stackoverflow.com/a/1988826/1558430
class memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}

    def __call__(self, n):
        digits = tuple(sorted(get_digits(n)))
        if digits in self.memo:
            return self.memo[digits]
        result = self.f(n)
        self.memo[digits] = result
        return result


def get_digits(n):
    return [i for i in str(n)]


def product(digits):
    digits = [int(i) for i in digits]
    return reduce(operator.mul, digits, 1)


def incremented(digits):



@memoize
def multiplicative_persistence(n):
    if not n:
        # We're done
        return 0
    digits = get_digits(n)
    if len(digits) == 1:
        return 0
    product_ = product(digits)
    return 1 + multiplicative_persistence(product_)


assert multiplicative_persistence(1) == 0
assert multiplicative_persistence(327) == 2
assert multiplicative_persistence(5428) == 2
assert multiplicative_persistence(9999) == 3
assert multiplicative_persistence(277777788888899) == 11


digits = ['1'] * 1000 + list('277777788888899')
while True:
    digits = incremented(digits)
    x = product(digits)
    if multiplicative_persistence(x) > 11:
        print('Record-breaker!', x)
    elif x % 1234567 == 0:
        print('Calculating', x)