# 그룹핑된 문자열에 이름 붙이기
import re

p = re.compile(r'(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)')
m = p.search('park 010-1234-1234')
print(m.group('name')) # park

p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')
print(p.search('Paris in the the spring').group()) # the the

# 전방 탐색
p = re.compile('.+:')
m = p.search('http://google.com')

print(m.group()) # http:

# 긍정형 전방 탐색
p = re.compile('.+(?=:)')
m = p.search('http://google.com')

print(m.group()) # http

# 부정형 전방 탐색
p = re.compile('.*[.](?!bat$).*$')

m = p.search('abc.bat')
print(m) # None
m = p.search('abc.exe')
print(m) # <_sre.SRE_Match object; span=(0, 7), match='abc.exe'>
