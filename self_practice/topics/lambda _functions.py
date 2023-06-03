
y = filter(lambda a: a >= 3, (1,2,3,4))  
print(list(y))


from functools import reduce

print(reduce(lambda a,b: a+b,[23,21,45,98]))


y = map(lambda a: a + 3, (1,2,3,4))  
print(list(y))