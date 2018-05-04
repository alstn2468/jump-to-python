# 클래스나 변수 등을 포함한 모듈
# mod2.py
PI = 3.141592
class Math :
    def solv(self, r) :
        return PI * (r ** 2)

def sum(a, b) :
    return a + b

if __name__ == '__main__' :
    print(PI)
    a = Math()
    print(a.solv(2))
    print(sum(PI, 4.4))

# 모듈에 포함된 변수, 클래스, 함수 사용하기
# print(mod2.PI) # 3.141592
# a = mod2.Math()
# print(a.solv(2)) # 12.566368
# print(mod2.sum(mod.PI, 4.4)) # 7.541592
