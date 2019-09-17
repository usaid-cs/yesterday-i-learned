class A:
    b = None
    _c = None
    __d = None

    def e(self):
        print(self.b, self._c, self.__d, getattr(self, '__e', None))


a = A()
print(a.b)
print(a._c)
#print(a.__d)  # Raises
a.e()

setattr(a, 'b', 1)
setattr(a, '_c', 2)
setattr(a, '__d', 3)
setattr(a, '__e', 4)
a.e()  # Prints 1 2 None 4 (__d is still None)