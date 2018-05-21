# 정규 표현식 사용 전
data = '''
park 800905-1049118
kim  700905-1059119
'''

result = []
for line in data.split('\n') :

    word_result = []

    for word in line.split(' ') :

        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit() :

            word = word[:6] + '-' + '*******'

        word_result.append(word)

    result.append(' '.join(word_result))

print('\n'.join(result))
