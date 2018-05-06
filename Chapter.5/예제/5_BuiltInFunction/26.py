# map
# two_times.py
def two_times(numberList) :
    result = []
    for number in numberList :
        result.append(number * 2)
    return result

result = two_times([1, 2, 3, 4])
print(result) # [2, 4, 6, 8]

def two_times(x) : return x * 2
print(list(map(two_times, [1, 2, 3, 4]))) # [2, 4, 6, 8]
print(list(map(lambda a : a * 2, [1, 2, 3, 4]))) # [2, 4 ,6, 8]

# map_test.py
def plus_one(x) :
    return x + 1
print(list(map(plus_one, [1, 2, 3, 4, 5]))) # [2, 3, 4, 5, 6]

# max
print(max([1, 2, 3])) # 3
print(max('python')) # 'y'

# min
print(min([1, 2, 3])) # 1
print(min('python')) # 'h'

# oct
print(oct(34)) # '0o42'
print(oct(12345)) # '0o30071'

# open
# f = open('binary_file', 'rb')
# fread = open('read_mode.txt', 'r')
# fread2 = open('read_mode.txt')
# fappend = open('append_mode.txt', 'a')
