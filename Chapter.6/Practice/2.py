'''
0 ~ 9까지의 문자로 된 숫자를 입력받았을 때,
이 입력값이 0 ~ 9까지의 모든 숫자가 각각 한 번씩만
사용된 것인지 확인하는 함수를 작성해 보자.

입력 예시 : 0123456789
출력 예시 : true

입력 예시 : 01234
출력 예시 : false

입력 예시 : 01234567890
출력 예시 : false

입력 예시 : 6789012345
출력 예시 : true

입력 예시 : 012322456789
출력 예시 : false
'''

def check_num(string) :
	result = []

	for num in string :
		if num not in result :
			result.append(num)

		else :
			return False

	return len(result) == 10

print(check_num('0123456789')) # True
print(check_num('01234')) # False
print(check_num('01234567890')) # False
print(check_num('6789012345')) # True
print(check_num('012322456789')) # True
