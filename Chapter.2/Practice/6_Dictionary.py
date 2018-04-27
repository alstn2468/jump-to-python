'''
딕셔너리 a에서 'B'에 해당되는 값을 추출하고 삭제해 보자.
'''

a = { 'A' : 90, 'B' : 80, 'C' : 70 }
result = a.pop('B')
print(a) # { 'A' : 90, 'C' : 70 }
print(result) # 80
