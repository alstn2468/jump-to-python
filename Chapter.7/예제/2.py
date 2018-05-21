# 정규 표현식 사용 후
import re

data = '''
park 800905-1049118
kim  700905-1059119
'''

pat = re.compile("(\d{6})[-]\d{7}")

print(pat.sub('\g<1>-*******', data))
