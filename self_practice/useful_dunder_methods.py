"""
__new__
__init__
__call__
__del__
__iter__
__next__
__repr__
__str__

__eq__
__ne__
__gt__
__lt__
__lte__
__gte__

__getitem__
__setitem__
__delitem__

__slots__
__doc__

__hash__

__len__
__contains__
"""

class A:

    def __init__(self) -> None:
        self.items = ["1"] * 3

    def __hash__(self) -> int:
        return hash(", ".join(self.items))
    


a = A()
print(hash(a))