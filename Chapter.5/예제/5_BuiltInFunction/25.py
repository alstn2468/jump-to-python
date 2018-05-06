# int
print(int('3')) # 3
print(int(3.4)) # 3
print(int('11', 2)) # 3
print(int('1A', 16)) # 26

# isinstance
class Person :
    pass

a = Person()
print(isinstance(a, Person)) # True
b = 3
print(isinstance(b, Person)) # False

# lambda
sum = lambda a, b : a + b
print(sum(3, 4)) # 7

myList = [lambda a, b : a + b, lambda a, b : a * b]
print(myList)
print(myList[0])
print(myList[0](3, 4)) # 7
print(myList[1](3, 4)) # 12

# len
print(len('python')) # 6
print(len([1, 2, 3])) # 3
print(len((1, 'a'))) # 2

# list
print(list('python')) # ['p', 'y', 't', 'h', 'o', 'n']
print(list((1, 2, 3))) # [1, 2, 3]
a = [1, 2, 3]
b = list(a)
print(b) # [1, 2, 3]
