# MULTILINE, M
import re

p = re.compile('^python\s\w+')

data = '''python one
life is too short
python two
you need python
python three'''

print(p.findall(data)) # ['python one']

p = re.compile('^python\s\w+', re.MULTILINE)

print(p.findall(data)) # ['python one', 'python two', 'python three']
