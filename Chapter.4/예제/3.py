# 함수 안에서 선언된 변수의 효력 범위
# vartest.py
a = 1
def vartest(a) :
    a = a + 1

vartest(a)
print(a) # 1

def vartest(hello) :
    hello = hello + 1

# vartest_error.py
# def vertest(a) :
#     a = a + 1
#
# vartest(3)
# print(a)
# 변수 a는 선언되지 않았다.

# 함수 안에서 함수 밖의 변수를 변경하는 방법
# retrun 이용하기
# vartest_return.py
a = 1
def vartest(a) :
    a = a + 1
    return a

a = vartest(a)
print(a) # 2

# global 명령어 이용하기
# vartest_global.py
a = 1
def vartest() :
    global a
    a = a + 1

vartest()
print(a) # 2
