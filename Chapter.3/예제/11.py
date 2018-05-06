# for와 함께 자주 사용하는 함수 range함수
a = range(10)
a # range(0, 10)
a = range(1, 11)
a # range(1, 11)

# range 함수의 예시
sum = 0
for i in range(1, 11) :
    sum = sum + i
print(sum) # 55
