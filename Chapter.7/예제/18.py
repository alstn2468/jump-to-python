import re

s = '<html><head><title>Title</title>'
print(len(s)) # 32

# Greedy
print(re.match('<.*>', s).span()) # (0, 32)
print(re.match('<.*>', s).group()) # <html><head><title>Title</title>

# Non-Greedy
print(re.match('<.*?>', s).group()) # <html>
