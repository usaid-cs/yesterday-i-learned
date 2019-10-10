from typing import List


def foo() -> list:
    return [1, 2, 3]


def foo2() -> List:
    return [1, 2, 3]


def foo3() -> List[int]:
    return [1, 2, 3]
