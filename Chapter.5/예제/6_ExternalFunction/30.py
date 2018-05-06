# OS 모듈
import os

# 내 시스템의 환경 변수값을 알고 싶을 때
print(os.environ)
print(os.environ['PATH'])

# 디렉터리 위치 변경하기
os.chdir('C:\WINDOWS')

# 디렉터리 위치 리턴받기
print(os.getcwd())

# 시스템 명령어 호출하기
os.system('dir')

# 실행한 시스템 명령어의 결과값 리턴받기
f = os.popen('dir')
print(f.read())

'''
os.mkdir(디렉터리) - 디렉터리를 생성한다.
os.rmdir(디렉터리) - 디렉터리를 삭제한다.
os.unlink(파일 이름) - 파일을 지운다.
os.rename(src, dst) - src라는 이름의 파일을 dst라는 이름으로 바꾼다.
'''
