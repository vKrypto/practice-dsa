# from enum import Enum

# from dataclasses import dataclass
# import inspect
# from functools import lru_cache




# class Node:
#     x: int
#     y: int


# print(f"{Node.__annotations__=}")


# point = Node()
# point.x = 4
# point.y = 4

# print(f"{point=}")




# @dataclass(frozen=False, slots=True)
# class Dimaond:    
#     x: int
#     y: int


#     def display(self):
#         return f">>>>{self.x, self.y}"

# obj = Dimaond({'y':5, 'x':6})
# print(f"{obj.display()}")
import functools


def divide(a, b):
	"Original Documentation of Divide"
	return a / b

half = functools.partial(divide, b = 2)
oneThird = functools.partial(divide, b = 3)

try:
	print(half.__name__)
except AttributeError:
	print('No Name')
print(half(4))




from functools import total_ordering


@total_ordering
class Students:
	def __init__(self, cgpa):
		self.cgpa = cgpa

	def __lt__(self, other):
		return self.cgpa<other.cgpa

	def __eq__(self, other):
		return self.cgpa == other.cgpa

Arjun = Students(8.6)

Ram = Students(7.5)

print(Arjun > Ram)
print(Arjun.__le__(Ram))
print(Arjun.__gt__(Ram))
print(Arjun.__ge__(Ram))
print(Arjun.__eq__(Ram))
print(Arjun.__ne__(Ram))







# class A:
#     ...


# class DogClass(A):
#     # __slots__ = ['name', 'color' ]

#     def __init__(self,name,color):
#         self.name = name
#         self.color = color
    
#     def bark(self):
#         if self.color == "black":
#             return True
#         else:
#             return False
# dc = DogClass('rudra','white')
# print(dc.__dict__)
# # Output: {'name': 'rudra', 'color': 'white'}

# print(type(DogClass))