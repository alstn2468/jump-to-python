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

# 결과값이 없는 함수
def sum(a, b) :
    print('%d, %d의 합은 %d입니다.' % (a, b, a + b))

sum(3, 4)
a = sum(3, 4)
print(a) # None

# 입력값도 결과값도 없는 함수
def say() :
    print('Hi')

say()

# 여러 개의 입력값을 받는 함수 만들기
def sum_many(*args) :
    sum = 0
    for i in args:
        sum = sum + i
    return sum

result = sum_many(1, 2, 3)
print(result) # 6
result = sum_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result) # 10

def sum_mul(choice, *args) :
    if choice == 'sum' :
        result = 0
        for i in args :
            result = result + i
    elif choice == 'mul' :
        result = 1
        for i in args :
            result = result * i
    return result

result = sum_mul('sum', 1, 2, 3, 4, 5)
print(result) # 15
result = sum_mul('mul', 1, 2, 3, 4, 5)
print(result) # 120

# 함수의 결과값은 언제나 하나
def sum_and_mul(a, b) :
    return a + b, a * b

result = sum_and_mul(3, 4) # (7, 12)
sum, mul = sum_and_mul(3, 4) # sum = 7, mul = 12

def sum_and_mul(a, b) :
    return a + b
    return a * b # 무시

result = sum_and_mul(2, 3)
print(result) # 5

# return의 또 다른 쓰임새
def say_nick(nick) :
    if nick == '바보' :
        return
    print('나의 별명은 %s입니다.' % nick)

say_nick('야호')
say_nick('바보')
