# search 객체의 매서드
import re

m = re.search('[a-z]+', '3 python')

print(m.group()) # 'python'
print(m.start()) # 2
print(m.end()) # 8
print(m.span()) # (2, 8)
