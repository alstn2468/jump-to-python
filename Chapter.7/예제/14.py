# 그룹핑
import re

p = re.compile('(ABC)+')
m = p.search('ABCABCABC OK?')

print(m)
# <_sre.SRE_Match object; span=(0, 9), match='ABCABCABC'>
print(m.group(0))
# ABCABCABC

p = re.compile(r'(\w+)\s+(\d+[-]\d+[-]\d+)')
m = p.search('park 010-1234-1234')

print(m.group(1))
# park
print(m.group(2))
# 010-1234-1234

p = re.compile(r'(\w+)\s+(\d+)[-]\d+[-]\d+')
m = p.search('park 010-1234-1234')

print(m.group(2))
# 010

p = re.compile(r'(\b\w+)\s+\1')
print(p.search('Paris in the the spring').group())
# the the
