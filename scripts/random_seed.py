import random


test_set_size = 10000000


def func1():
    eh = []
    for _ in range(test_set_size):
        eh.append(random.randint(0, test_set_size))
    return len(set(eh))


def func2():
    eh = []
    for _ in range(test_set_size):
        ran = random.randint(0, test_set_size)
        eh.append(ran)
        random.seed(ran)
    return len(set(eh))


print(func1())
print(func2())