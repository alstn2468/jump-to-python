# 게시판 페이징하기
def getTotalPage(m, n) :
    if m % n == 0 :
        return m // n
    else :
        return m // n + 1

print(getTotalPage(5, 10)) # 1
print(getTotalPage(15, 10)) # 2
print(getTotalPage(25, 10)) # 3
print(getTotalPage(30, 10)) # 3
