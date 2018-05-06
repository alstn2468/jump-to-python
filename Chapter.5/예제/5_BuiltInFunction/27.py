# ord
print(ord('a')) # 97
print(ord('0')) # 48

# pow
print(pow(2, 4)) # 16
print(pow(3, 3)) # 27

# range

# 인수가 하나인 경우
print(list(range(5))) # [0, 1, 2, 3, 4]

# 인수가 2개인 경우
print(list(range(5, 10))) # [5, 6, 7, 8, 9]

# 인수가 3개인 경우
print(list(range(1, 10, 2))) # [1, 3, 5, 7, 9]
print(list(range(0, -10, -1))) # [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]

# sorted
print(sorted([3, 1, 2])) # [1, 2, 3]
print(sorted(['a', 'c', 'b'])) # ['a', 'b', 'c']
print(sorted('zero')) # ['e', 'o', 'r', 'z']
print(sorted((3, 2, 1))) # [1, 2, 3]

# sort 함수와의 차이점
a = [3, 1, 2]
result = a.sort()
print(result) # None
print(a) # [1, 2, 3]

# str
print(str(3)) # '3'
print(str('hi')) # 'hi'
print(str('hi'.upper())) # 'HI'

# tuple
print(tuple('abc')) # ('a', 'b', 'c')
print(tuple([1, 2, 3])) # (1, 2, 3)
print(tuple((1, 2, 3))) # (1, 2, 3)

# type
print(type('abc')) # <class 'str'>
print(type([])) # <class 'list'>
print(type(open('test', 'w'))) # <class '_io.TextIOWrapper'>

# zip
print(list(zip([1, 2, 3], [4, 5, 6]))) # [(1, 4), (2, 5), (3, 6)]
print(list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))) #[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
print(list(zip('abc', 'def'))) # [('a', 'd'), ('b', 'e'), ('c', 'f')]
