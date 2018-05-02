# self 살펴보기
class Service :
    secret = '영구는 배꼽이 두 개다.'
    def sum(self, a, b) :
        result = a + b
        print('%s + %s = %s입니다.' % (a, b, result))

pey = Service()
Service.sum(pey, 1, 1)
pey.sum(1, 1)
