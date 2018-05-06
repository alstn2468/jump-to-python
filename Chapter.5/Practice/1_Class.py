'''
다음과 같이 동작하는 클래스 Calculator를 작성해 보자.
>>> cal1 = Calculator([1, 2, 3, 4, 5,])
>>> cal1.sum()
15
>>> cal1.avg()
3.0
>>> cal2 = Calculator([6, 7, 8, 9, 10])
>>> cal2.sum()
40
>>> cal2.avg()
8.0
'''

class Calculator :
    def __init__(self, data) :
        self.data = data

    def sum(self) :
        result = 0
        for data in self.data :
            result += data
        return result

    def avg(self) :
        return sum(self.data) / len(self.data)

cal1 = Calculator([1, 2, 3, 4, 5,])
print(cal1.sum()) # 15
print(cal1.avg()) # 3.0

cal2 = Calculator([6, 7, 8, 9, 10])
print(cal2.sum()) # 40
print(cal2.avg()) # 8.0
