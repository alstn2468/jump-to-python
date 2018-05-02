# 사칙연산 클래스 만들기
#
# 목표
# a = FourCal()
# a.setdata(4,2)
# print(a.sum()) # 6
# print(a.mul()) # 8
# print(a.sub()) # 2
# print(a.div()) # 2

# 클래스 구조 만들기
class FourCal :
    pass

a = FourCal()
print(type(a)) # <class '__main__.FourCal'>

# 객체에 숫자 지정할 수 있게 만들기
class FourCal :
    def setdata(self, first, second) :
        self.first = first
        self.second = second

a = FourCal()
a.setdata(4, 2)
print(a.first) # 4
print(a.second) # 2

b = FourCal()
b.setdata(3, 7)
print(b.first) # 3
print(a.first) # 4

# 더하기 기능 만들기
class FourCal :
    def setdata(self, first, second) :
        self.first = first
        self.second = second

    def sum(self) :
        result = self.first + self.second
        return result

a = FourCal()
a.setdata(4, 2)
print(a.sum()) # 6
