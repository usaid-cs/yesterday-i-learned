class MyCircularQueue:
    q = None
    head = 0
    tail = 0
    length = None

    def __init__(my, k: int):
        my.q = [None] * k
        my.length = 0

    def enQueue(self, value: int) -> bool:
        # print('nq', self.q, self.head, self.tail, self.length)
        if self.isFull():
            return False
        if self.q[self.tail] is None and self.length == 0:
            # edge case of length 0
            self.q[self.tail] = value
        else:
            self.tail = (self.tail + 1) % len(self.q)
            assert self.q[self.tail] is None
            self.q[self.tail] = value
        self.length += 1
        assert self.length <= len(self.q)
        # print('nq 2', self.q, self.head, self.tail, self.length)
        return True

    def deQueue(self) -> bool:
        # print('dairy queen', self.q, self.head, self.tail, self.length)
        if self.isEmpty():
            return False
        if self.q[self.head] is None:
            return False
        assert self.q[self.head] is not None
        if self.tail == self.head and self.length == 1:
            # special case for queue of length 1
            self.q[self.tail] = None
            self.length = 0
            return True
        self.q[self.head] = None
        self.head += 1  # [None, 2H, 3T] -> [None, None, 3HT]
        self.head = self.head % len(self.q)
        self.length = max(0, self.length - 1)
        # print('dairy queen 2', self.q, self.head, self.tail, self.length)
        return True

    def Front(self) -> int:
        # print('front', self.q)
        if self.isEmpty():
            return -1
        foo = self.q[self.head]
        if foo is None:
            return -1
        return foo

    def Rear(self) -> int:
        # print('rear', self.q)
        if self.isEmpty():
            return -1
        foo = self.q[self.tail]
        if foo is None:
            return -1
        return foo

    def isEmpty(self) -> bool:
        # print('isempty', self.q)
        return self.length == 0

    def isFull(self) -> bool:
        # print('isfull', self.q)
        return self.length == len(self.q)



# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
#
#   H     T
#   1 2 3 4 - - -
#
#   T     H       T'
#   8 - - 4 5 6 7
#                 8 9 0
