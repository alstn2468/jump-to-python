# 변수
a = 1
b = "python"
c = [1, 2, 3]

a = 3
type(3) # <class 'int'>

a = 3
b = 3
a is b # True

# a, b, c는 정말 같은 객체를 가리키는 걸까?
import sys
sys.getrefcount(3) # 30
a = 3
sys.getrefcount(3) # 31
b = 3
sys.getrefcount(3) # 32
c = 3
sys.getrefcount(3) # 33

# 변수를 만드는 여러 가지 방법
a, b = ('python', 'life')
(a, b) = 'python', 'life'
[a, b] = ['python', 'life']
a = b = 'python'

a = 3
b = 5
a, b = b, a
a # 5
b # 3

# 메모리에 생성된 변수 없애기
a = 3
b = 3
del(a)
del(b)

# 리스트를 변수에 넣고 복사하고자 할 때
a = [1, 2, 3]
b = a
a[1] = 4
a # [1, 4, 3]
b # [1, 4, 3]

# 1. [:] 이용
a = [1, 2, 3]
b = a[:]
a[1] = 4
a # [1, 4, 3]
b # [1, 2, 3]

# 2. copy 모듈 이용
from copy import copy
b = copy(a)
b is a # False
