# match 객체의 매서드
import re

p = re.compile('[a-z]+')

m = p.match('python')

print(m.group()) # 'python'
print(m.start()) # 0
print(m.end()) # 6
print(m.span()) # (0, 6)
