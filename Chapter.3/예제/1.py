# if문
money = 1
if money :
    print("택시를 타고 가라")
else :
    print("걸어 가라")

# 들여쓰기
if money :
    print("택시를")
print("타고")
    # print("가자") Error

if money :
    print("택시를")
    print("타고")
        # print("가자") Error

# 비교 연산자
x = 3
y = 2
x > y # True
x < y # False
x == y # False
x != y # True

money = 2000
if money >= 3000 :
    print("택시를 타고 가라")
else :
    print("걸어 가라")

# and, or, not
money = 2000
card = 1
if money >= 3000 or card :
    print("택시를 타고 가라")
else :
    print("걸어 가라")

# x in s, x not in s
1 in [1, 2, 3] # True
1 not in [1, 2, 3] # False
'a' in ('a', 'b', 'c') # True
'j' not in 'python' # True

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket :
    print('택시를 타고 가라')
else :
    print('걸어 가라')

# 조건문에서 아무 일도 하지 않게 설정하고 싶다면
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket :
    pass # pass가 수행되고 아무런 결과값을 보여주지 않는다.
else :
    print("카드를 꺼내라")

# 다양한 조건을 판단하는 elif
pocket = ['paper', 'cellphone']
card = 1
if 'money' in pocket :
    print("택시를 타고 가라")
else :
    if card :
        print("택시를 타고 가라")
    else :
        print("걸어 가라")

pocket = ['paper', 'cellphone']
caed = 1
if 'money' in pocket :
    print("택시를 타고 가라")
elif card :
    print("택시를 타고 가라")
else :
    print("걸어 가라")

# if문을 한 줄로 작성하기
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket : pass
else : print("카드를 꺼내라")
