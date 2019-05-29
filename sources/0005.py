class Slotted:
    __slots__ = ()

class NotSlotted:
    pass

slotted = Slotted()
not_slotted = NotSlotted()

slotted.a = 5
not_slotted.a = 5