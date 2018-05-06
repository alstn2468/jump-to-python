# 클래스
# 클래스가 필요한 이유
result = 0

def adder(num) :
    global result
    result += num
    return result

print(adder(3)) # 3
print(adder(4)) # 7
