# 내가 프로그램을 만들 수 있을까?
def GuGu(n) :
    result = []
    i = 1
    while i < 10 :
        result.append(n * i)
        i = i + 1
    return result

print(GuGu(2)) # [2, 4, 6, 8, 10, 12, 14, 16, 18]
