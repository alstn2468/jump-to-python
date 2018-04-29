# sys 모듈로 입력 인수 주기
# sys1.py
import sys

args = sys.argv[1:]
for i in args :
    print(i)

'''
C:\Python>python sys1.py aaa bbb ccc
aaa
bbb
ccc
'''

# sys2.py
import sys
args = sys.argv[1:]
for i in args :
    print(i.upper(), end = ' ')

'''
C:\Python>python sys2.py life is too short, you need python
LIFE IS TOO SHORT, YOU NEED PYTHON
'''
