# IGNORECASE, I
import re

p = re.compile('[a-z]', re.I)

print(p.match('python')) # <_sre.SRE_Match object; span=(0, 1), match='p'>
print(p.match('Python')) # <_sre.SRE_Match object; span=(0, 1), match='p'>
print(p.match('PYTHON')) # <_sre.SRE_Match object; span=(0, 1), match='p'>
