# 문자열 바꾸기
import re

# sub 매서드
p = re.compile('(blue|white|red)')

print(p.sub('colour', 'blue socks and red shoes'))
# colour socks and colour shoes
print(p.sub('colour', 'blue socks and red shoes', count = 1))
# colour socks and red shoes

# subn 매서드
print(p.subn('colour', 'blue socks and red shoes'))
# ('colour socks and colour shoes', 2)

# sub 매서드 사용 시 참조 구문 사용하기
p = re.compile(r'(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)')

print(p.sub('\g<phone> \g<name>', 'park 010-1234-1234'))
# 010-1234-1234 park
print(p.sub('\g<2> \g<1>', 'park 010-1234-1234'))
# 010-1234-1234 park
