# 함수

# 파이썬 함수의 구조
def sum(a, b) :
    return a + b

a = 3
b = 4
c = sum(a,b)
print(c) # 7

# 일반적인 함수
def sum(a, b) :
    result = a + b
    return result

a = sum(3, 4)
print(a) # 7

# 입력값이 없는 함수
def say() :
    return 'Hi'

a = say()
print(a) # Hi

# 결과 값이 없는 함수
