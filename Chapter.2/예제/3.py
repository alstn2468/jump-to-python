# 'Pithon'이라는 문자열을 'Python'으로 바꾸기
a = "Pithon"
a[1] # 'i'
a[1] = 'y'

a = "Pithon"
a[:1] # 'P'
a[2:] # 'thon'
a[:1] + 'y' + a[2:] # 'Python'

# "Error is %d%" % 98
"Error is %d%%." % 98 # 'Error is 98%.'
