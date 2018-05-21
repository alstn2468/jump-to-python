# finditer
import re

p = re.compile('[a-z]+')

result = p.finditer('life is too short')

print(result) # <callable_iterator object at 0x032EA230>

for r in result :
    print(r)
'''
<_sre.SRE_Match object; span=(0, 4), match='life'>
<_sre.SRE_Match object; span=(5, 7), match='is'>
<_sre.SRE_Match object; span=(8, 11), match='too'>
<_sre.SRE_Match object; span=(12, 17), match='short'>
'''
