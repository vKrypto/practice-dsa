import math

def is_prime(n):
    # Handle small numbers and edge cases
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Check for factors from 5 to sqrt(n)
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    
    return True

# Example usage
# print(is_prime(29))  # True
# print(is_prime(15))  # False

print(is_prime(901))


"""
1 -> n
for i in range(n)
1 -> sqrt(n)
for i in range(1, sqrt(n))
1 -> sqrt(n) (ignore even numbers)
for i in range(1, sqrt(n), 2)

5,_,7,_,_
1 -> sqrt(n) (ignore even numbers,and block size = 6)
for i in range(1, sqrt(n), 6):
    if n % i == 0 or n % (i + 2) == 0:
        return False

time complexity : omega(sqrt(n)/6), o(sqrt(n))
 
"""

# import pdb

# def add(a, b):
#     pdb.set_trace()
#     return a + b

# print(add(3, 4))
from functools import wraps

def repeat(n):
    
    @wraps
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hello(a, b):
    print("Hello!", a, b)

say_hello(3,4)
