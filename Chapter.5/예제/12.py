# 초깃값 설정하기
class HousePark :
    lastname = "박"
    def __init__(self, name) :
        self.fullname = self.lastname + name

    def travel(self, where) :
        print('%s, %s여행을 가다.' % (self.fullname, where))

pey = HousePark('응용')
pey.travel('태국')
