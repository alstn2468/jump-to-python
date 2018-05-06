# 프로그램 외부에 저장된 파일을 읽는 여러 가지 방법
# readline() 함수 이용하기
# readline.py
f = open('C:/Python/새파일.txt', 'r')
line = f.readline() # 한 줄 읽어오기
print(line)
f.close()

# 모든 라인을 읽어오고 싶다면
# readline_all.py
f = open('C:/Python/새파일.txt', 'r')
while True :
    line = f.readline()
    if not line : break
    print(line)
f.close()

# 사용자의 입력을 받아서 출력하는 경우
# 입력을 받는 방식만 다르다.
while 1 :
    data = input()
    if not data : break
    print(data)

# readlines() 함수 이용하기
f = open('C:/Python/새파일.txt', 'r')
lines = f.readlines() # 모든 라인을 읽어서 각각의 줄을 요소로 갖는 리스트 리턴
for line in lines :
    print(line)
f.close()

# read() 함수 이용하기
f = open('C:/Python/새파일.txt', 'r')
data = f.read() # 파일 내용의 전체를 문자열로 리턴
print(data)
f.close()
