# Code review 2020-01-31 edition

class Rohit(int):
    def __eq__(self, other):
        return other == 0
    def __ne__(self, other):
        return bool(other)
    def __le__(self, other):
        return False


class Alex(list):
    def __len__(self):
        return Rohit(0)


a = Alex()
a.append(1)

assert a == [1]
# It's empty, you see
assert not a
assert len(a) <= 0
assert len(a) == 0
assert bool(a) == False