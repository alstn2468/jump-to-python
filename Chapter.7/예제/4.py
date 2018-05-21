# search
import re

p = re.compile('[a-z]+')

m = p.search('python')

print(m) # <_sre.SRE_Match object; span=(0, 6), match='python'>

m = p.search('3 python')

print(m) # <_sre.SRE_Match object; span=(2, 8), match='python'>
