'''
문자열을 입력 받아 같은 문자가 연속적으로 반복되는 경우에
그 반복 횟수를 표시해 문자열을 압축하여 표시해 보자.

입력 예시 : aaabbcccccca
출력 예시 : a3b2c6a1
'''

def zip_string(string) :
	_char = ""
	count = 0
	result = ""

	for char in string :
		if char != _char :
			_char = char

			if count :
				result += str(count)
			result += char
			count = 1

		else :
			count += 1

	if count :
		result += str(count)

	return result

print(zip_string('aaabbcccccca')) # a3b2c6a1
