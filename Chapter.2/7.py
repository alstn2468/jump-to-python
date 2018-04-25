# 딕셔너리

# 딕셔녀리 예
dic = { 'name' : 'pey', 'phone' : '0119993323', 'birth' : '1118' }
'''
Key     Value
name    pey
phone   0119993323
birth   1118
'''

a = { 1 : 'hi' } # Key : 1, Value : 'hi'
a = { 'a' : [1, 2, 3] } # Key : 'a', Value : [1, 2, 3]

# 딕셔너리 쌍 추가하기
a = { 1 : 'a' }
a[2] = 'b'
a # { 2 : 'b', 1 : 'a' }
a['name'] = 'pey'
a # { 'name' : 'pey', 2 : 'b', 1 : 'a' }
a[3] = [1, 2, 3]
a # { 'name' : 'pey', 3 : [1, 2, 3], 2 : 'b', 1 : 'a' }

# 딕셔너리 요소 삭제하기
del a[1]
a # { 'name' : 'pey', 3 : [1, 2, 3], 2 : 'b' }
