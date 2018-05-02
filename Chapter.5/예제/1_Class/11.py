# '박씨네 집' 클래스 만들기
#
# 목표
# pey = HousePark()
# print(pey.lastname) # 박
# pey.setname('응용')
# print(pey.fullname) # 박응용
# pey.travel('부산') # 박응용, 부산여행을 가다.

# 클래스 기능 만들기
class HousePark :
    lastname = "박"
    def setname(self, name) :
        self.fullname = self.lastname + name

    def travel(self, where) :
        print('%s, %s여행을 가다.' % (self.fullname, where))

pey = HousePark()
pey.setname('응용')
pes = HousePark()
print(pey.lastname) # 박
print(pes.lastname) # 박
print(pey.fullname) # 박응용
pey.travel('부산')

# __init__ 사용 전
# pey = HousePark()
# pey.travel('부산') ERROR
