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