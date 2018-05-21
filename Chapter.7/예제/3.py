# match
import re

p = re.compile('[a-z]+')

m = p.match('python')
print(m) # <_sre.SRE_Match object; span=(0, 6), match='python'>

m = p.match('3 python')
print(m) # None

'''
p = re.compile(정규 표현식)
m = p.match('조사할 문자열')

if m :
    print('Match found : ', m.group())

else :
    print('No match')
'''
