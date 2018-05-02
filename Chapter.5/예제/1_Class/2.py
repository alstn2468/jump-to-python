# 한 프로그램에서 2개의 계산기가 필요한 상황
result1 = 0
result2 = 0

def adder1(num) :
    global result1
    result1 += num
    return result1
def adder2(num) :
    global result2
    result2 += num
    return result2

print(adder1(3)) # 3
print(adder1(4)) # 7
print(adder2(3)) # 3
print(adder2(7)) # 10
