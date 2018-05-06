# 조건에 맞지 않는 경우 맨 처음으로 돌아가기
a = 0
while a < 10 :
    a = a + 1
    if a % 2 == 0 : continue
    print(a)

# 무한 루프
while True :
    print('Ctrl + C를 눌러야 while문을 빠져나갈 수 있습니다.')
