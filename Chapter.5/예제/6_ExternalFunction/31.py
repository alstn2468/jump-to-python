# shutil
# 파일 복사하기
import shutil
#shutil.copy('src.txt', 'dst.txt')

# glob
# 디렉터리에 있는 파일들을 리스트로 만들기
import glob
print(glob.glob('C:/*'))

# tempfile
import tempfile
filename = tempfile.mktemp()
print(filename)

f = tempfile.TemporaryFile()
f.close()

# time
import time

# 1970년 1월 1일 0시 0분 0초를 기준으로 지난 시간을 초 단위로 리턴
print(time.time())

# time.time()으로 반환된 실수로 연도, 달, 월, 시, 분, 초 로 바꾸어주는 함수
print(time.localtime(time.time()))

# time.localtime()에 의해서 반환된 튜플 형태 값으로 알아보기 쉬운 형태로 리턴하는 함수
print(time.asctime(time.localtime(time.time())))

# 현재 시간 리턴
print(time.ctime())

# 시간에 관계된 것을 세밀하게 표현할 수 있는 여러가지 포맷 제공
print(time.strftime('%x', time.localtime(time.time())))
print(time.strftime('%c', time.localtime(time.time())))

# sleep1.py
for i in range(10) :
    print(i)
    time.sleep(1)
