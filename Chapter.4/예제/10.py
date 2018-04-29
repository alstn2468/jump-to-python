# 파일에 새로운 내용 추가하기
# adddata.py
f = open('C:/Python/새파일.txt', 'a')
for i in range(11, 20) :
    data = '%d번째 줄입니다.\n' % i
    f.write(dat)
f.close()

# with문과 함께 사용하기
# 지금 까지의 방식
f = open('foo.txt', 'w')
f.write('Life is too short, you need python')
f.close()

# with 블록을 벗어나는 순간 f가 자동으로 close()
with open('foo.txt', 'w') as f :
    f.write('Life is too short, you need python')
