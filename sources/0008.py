a = 0

def foo():
    global a
    print(a)
    a = 1


foo()
print(a)

def bar():
    a = 4
    def baz():
        nonlocal a
        print(a)
    baz()

bar()
