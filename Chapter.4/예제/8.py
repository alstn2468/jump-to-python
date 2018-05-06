# 파일을 쓰기 모드로 열어 출력값 적기
# writedata.py
f = open('C:/Python/새파일.txt', 'w')
for i in range(1, 11) :
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# 두 방법의 차이점은 print 대신 파일 객체 f의 write 함수를 이용한 것
for i in range(1, 11) :
    data = "%d번째 줄입니다.\n" % i
    print(data)
