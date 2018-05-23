import re

# | 메타 문자 - or과 동일한 의미
p = re.compile('Crow|Servo')
m = p.match('CrowHello')
print(m)
# <_sre.SRE_Match object; span=(0, 4), match='Crow'>

# ^ 메타 문자 - 문자열의 처음
print(re.search('^Life', 'Life is too short'))
# <_sre.SRE_Match object; span=(0, 4), match='Life'>
print(re.search('^Life', 'My Life'))
# None

# $ 메타 문자 - 문자열의 끝
print(re.search('short$', 'Life is too short'))
# <_sre.SRE_Match object; span=(12, 17), match='short'>
print(re.search('short$', 'Life is too shrot, you need python'))
# None

# \A == ^, \Z == $ -> MULTILINE 사용시 전체 문자열 기준

# \b 단어 구분자
p = re.compile(r'\bclass\b')
print(p.search('no class at all'))
# <_sre.SRE_Match object; span=(3, 8), match='class'>
print(p.search('the declassfied algorithm'))
# None
print(p.search('one subclass is'))
# None

# \B 메타 문자
p = re.compile(r'\Bclass\B')
print(p.search('no class at all'))
# None
print(p.search('the declassfied algorithm'))
# <_sre.SRE_Match object; span=(6, 11), match='class'>
print(p.search('one subclass is'))
# None
