# 오류 회피하기
try :
    f = open('없는 파일.txt', 'r')
except FileNotFoundError :
    pass

# 오류 일부러 발생시키기
class Bird :
    def fly(self) :
        raise NotImplementedError

class Eagle(Bird) :
    pass

# eagle = Eagle()
# eagle.fly() # 'NotImplementedError'

class Eagle(Bird) :
    def fly(self) :
        print('very fast')

eagle = Eagle()
eagle.fly() # 'very fast'
