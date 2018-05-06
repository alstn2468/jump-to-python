# filter
# positive.py
def positive(numberList) :
    result = []
    for num in numberList :
        if num > 0 :
            result.append(num)
    return result

print(positive([1, -3, 2, 0, -5, 6])) # [1, 2, 6]

# filter1.py
def positive(x) :
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6]))) # [1, 2, 6]
print(list(filter(lambda x : x > 0, [1, -3, 2, 0, -5, 6]))) # [1, 2, 6]

# hex
print(hex(234)) # '0xea'
print(hex(3)) # '0x3'

# id
a = 3
print(id(3)) # 주소값
print(id(a)) # 주소값
b = a
print(id(b)) # 주소값
# 3, a, b 모두 같은 주소값, 같은 객체를 가리킨다.
print(id(4))

# input
a = input()
print(a)
b = input('Enter : ')
print(b)
