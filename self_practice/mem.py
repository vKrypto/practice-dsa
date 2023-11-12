import sys
from pprint import pprint

class A:


    """
    object -->
        *_gc_next == 8
        *_gc_prev  == 8
    
        obj_refcnt == 8 
        *obj_type == 8

        *__dict__ === 8 , stores all the variables, methods
        *__weakref__ == 8,
    """

    def __init__(self) -> None:
        pass


print({A.__basicsize__})  # 32
print(sys.getsizeof(A()))  # 48
pprint(A.__dict__)  
# {
#     '__module__': '__main__', 
#     '__init__': <function A.__init__ at 0x7f1d8f210540>, 
#     '__dict__': <attribute '__dict__' of 'A' objects>, 
#     '__weakref__': <attribute '__weakref__' of 'A' objects>, 
#     '__doc__': '--,....'
# }


class B:
    __slots__ = ()

    """
    object -->
        *_gc_next == 8
        *_gc_prev  == 8
    
        obj_refcnt == 8 
        *obj_type == 8
    """


    def __init__(self) -> None:
        pass


print({B.__basicsize__})  # 16
print(sys.getsizeof(B()))  # 32
pprint(B.__dict__)
# {
#     '__module__': '__main__', 
#     '__slots__': (), 
#     '__init__': <function B.__init__ at 0x7fda49b545e0>,
#     '__doc__': None
# }


class C:
    __slots__ = ('x', 'y')

    """
    object -->
        *_gc_next == 8
        *_gc_prev  == 8
    
        obj_refcnt == 8 
        *obj_type == 8

        *x == 8
        *y == 8

    """
    pass

print({C.__basicsize__})  # 32
print(sys.getsizeof(C()))  # 48
# print(C.__dict__)
# {
#     '__module__': '__main__', 
#     '__slots__': ('x', 'y'), 
#     '__doc__': None,
#     'x': <member 'x' of 'C' objects>, 
#     'y': <member 'y' of 'C' objects>,
# }


class D(C):

    """
    object -->
        *_gc_next == 8
        *_gc_prev  == 8
    
        obj_refcnt == 8 
        *obj_type == 8

        *__dict__ === 8 , stores all the variables, methods
        *__weakref__ == 8,
    """
    pass

print(f"{D.__basicsize__=}")  # 40
print(f"{sys.getsizeof(D())=}")  # 72
print(D().__dict__)
