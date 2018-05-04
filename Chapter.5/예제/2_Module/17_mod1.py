# 모듈
# mod1.py

def sum(a, b) :
    return a + b

# import mod1
# print(mod1.sum(3, 4)) # 7

def safe_sum(a, b) :
    if type(a) != type(b) :
        print('더할수 있는 값이 아닙니다.')
        return
    else :
        result = sum(a, b)

    return result

# import mod1
# print(mod1.safe_sum(3, 4)) # 7
# print(mod1.safe_sum(1, 'a')) # 더할수 있는 값이 아닙니다. NONE
# print(mod1.sum(10, 20)) # 30

if __name__ == '__main__' :
    print(safe_sum('a', 1))
    print(safe_sum(1, 4))
    print(sum(10, 10.4))
