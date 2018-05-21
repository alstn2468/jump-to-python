# findall
import re

p = re.compile('[a-z]+')

result = p.findall('life is too short')

print(result) # ['life', 'is', 'too', 'short']
