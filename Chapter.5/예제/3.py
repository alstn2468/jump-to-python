# 클래스 이용
class Calculator :
    def __init__(self) :
        self.result = 0

    def adder(self, num) :
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.adder(3)) # 3
print(cal1.adder(4)) # 7
print(cal2.adder(3)) # 3
print(cal2.adder(7)) # 10
