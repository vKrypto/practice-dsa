

# A generator function
def simpleGeneratorFun():
    print("calling function next")
    for i in range(3):
        print("ruinning next ", i)
        yield i

# x is a generator object
x = simpleGeneratorFun()

print("x is a generator function", x)
# Iterating over the generator object using next
print(next(x)) # In Python 3, __next__()
print(next(x))
print(next(x))
print(next(x))