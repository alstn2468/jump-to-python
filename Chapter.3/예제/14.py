# 리스트 안에 for문 포함하기
a = [1, 2, 3, 4]
result = []
for num in a :
    result.append(num * 3)
print(result) # [3, 6, 9, 12]

# 리스트 내포를 이용한 간단한 해결 방식
result = [num * 3 for num in a]
print(result) # [3, 6, 9, 12]

# 짝수에만 3을 곱하여 담고 싶다면
result = [num * 3 for num in a if num % 2 == 0]
print(result) # [6, 12]

# 구구단의 모든 결과에 리스트에 담기
result = [x * y for x in range(2, 10) for y in range(1, 10)]
print(result)
