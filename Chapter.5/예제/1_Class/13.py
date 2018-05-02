# 클래스의 상속
class HousePark :
    lastname = "박"
    def __init__(self, name) :
        self.fullname = self.lastname + name

    def travel(self, where) :
        print('%s, %s여행을 가다.' % (self.fullname, where))

class HouseKim(HousePark) :
    lastname = '김'

juliet = HouseKim('줄리엣')
juliet.travel('독도')
