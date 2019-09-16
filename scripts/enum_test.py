from enum import Enum

class Foo(Enum):
    a = 1
    b = 2
    c = 3

def bar(foo: Foo):
    return foo


bar(Foo.a)
bar(1)  # Fails