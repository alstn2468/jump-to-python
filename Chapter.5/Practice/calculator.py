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

if __name__ == '__main__' :
    cal1 = Calculator([1, 2, 3, 4, 5,])
    print(cal1.sum()) # 15
    print(cal1.avg()) # 3.0

    cal2 = Calculator([6, 7, 8, 9, 10])
    print(cal2.sum()) # 40
    print(cal2.avg()) # 8.0
