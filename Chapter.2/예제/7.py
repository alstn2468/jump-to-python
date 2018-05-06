# 딕셔너리
# 딕셔녀리의 표현
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

# 딕셔너리에서 Key 사용해 Value 얻기
grade = { 'pey' : 10, 'julliet' : 99 }
grade['pey'] # 10
grade['julliet'] # 99
a = { 1 : 'a', 2 : 'b' }
a[1] # 'a'
a[2] # 'b'
a = { 'a' : 1, 'b' : 2 }
a['a'] # 1
a['b'] # 2
dic = { 'name' : 'pey', 'phone' : '0119993323', 'birth' : '1118' }
dic['name'] # 'pey'
dic['phone'] # '0119993323'
dic['birth'] # '1118'


# 딕셔너리 만들 때 주의할 사항
a = { 1 : 'a', 1 : 'b' }
a # { 1 : 'b' } 동일한 Key는 사용할 수 없음
# a = { [1, 2] : 'hi' } 변하는 값은 Key로 사용할 수 없음

# Key 리스트 만들기
a = { 'name' : 'pey', 'phone' : '0119993323', 'birth' : '1118' }
a.keys() # dic_keys(['name', 'phone', 'birth'])
for k in a.keys() :
    print(k)
'''
name
phone
birth
'''

# dict_keys 객체를 리스트로 반환
list(a.keys()) # ['phone', 'birth', 'name']

# Value 리스트 만들기
a.values() # dic_values(['pey', '0119993323', '1118'])

# Key, Value 쌍 얻기
a.items() # dict_items([('name', 'pey'), ('phone', '0119993323'), ('birth', '1118')])

# Key, Value 쌍 모두 지우기
a.clear()
a # ()

# Key로 Value 얻기
a = { 'name' : 'pey', 'phone' : '0119993323', 'birth' : '1118' }
a.get('name') # 'pey'
a.get('phone') # '0119993323'
a.get('nokey') # None
# a['nokey'] Error
a.get('foo', 'bar') # default값인 'bar' 반환

# Key가 딕셔너리 안에 있는지 조사하기
a = { 'name' : 'pey', 'phone' : '0119993323', 'birth' : '1118' }
'name' in a # True
'email' in a # False
