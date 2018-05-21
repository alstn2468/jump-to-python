# DOTALL, S
import re

p = re.compile('a.b')

m = p.match('a\nb')

print(m) # None

p = re.compile('a.b', re.DOTALL)

m = p.match('a\nb')

print(m) # <_sre.SRE_Match object; span=(0, 3), match='a\nb'>
