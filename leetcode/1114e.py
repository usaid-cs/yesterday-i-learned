# Not a good solution. Use threading.Lock instead if you have access to imports.
class Foo:

    mutex = 0

    def __init__(self):
        pass


    def first(self, printFirst: 'Callable[[], None]') -> None:
        while self.mutex != 0:
            pass
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.mutex = 1

    def second(self, printSecond: 'Callable[[], None]') -> None:
        while self.mutex != 1:
            pass
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.mutex = 2

    def third(self, printThird: 'Callable[[], None]') -> None:
        while self.mutex != 2:
            pass
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        self.mutex = 3
