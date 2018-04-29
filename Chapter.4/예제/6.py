# print자세히 알기
a = 123
print(a) # 숫자 출력하기
a = 'Python'
print(a) # 문자열 출력하기
a = [1, 2, 3]
print(a) # 리스트 출력하기

# 큰따옴표(")로 둘러싸인 문자열을 + 연산과 동일
print("life""is""too short")
print("life" + "is" + "too short")

# 문자열 띄어쓰기는 콤마로 한다.
print("life", "is", "too short")

# 한 줄에 결과값 출력하기
for i in range(10) :
    print(i, end = ' ')
