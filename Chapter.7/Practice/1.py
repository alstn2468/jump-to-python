'''
다음 중 정규식 "a[.]{3,}b"과
매치되는 문자열은 무엇일 까?

A. acccb
B. a....b
C. aaab
D. a.cccb
'''

import re

p = re.compile("a[.]{3,}b")

print(p.match('acccb')) # None
print(p.match('a....b')) # <_sre.SRE_Match object; span=(0, 6), match='a....b'>
print(p.match('aaab')) # None
print(p.match('a.cccb')) # None

# 답 : B
