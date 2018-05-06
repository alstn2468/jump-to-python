# 고급 문자열 포매팅
# 숫자 바로 대입하기
"I eat {0} apples".format(3) # 'I eat 3 apples'

# 문자열 바로 대입하기
"I eat {0} apples".format("five") # 'I eat five apples'

# 숫자 값을 가진 변수를 대입하기
number =3
"I eat {0} apples".format(number) # 'I eat 3 apples'

# 2개 이상의 값 넣기
number = 10
day = "three"
"I ate {0} apples. so I was sick for {1} days.".format(number, day)
# 'I ate 10 apples. so I was for three days.'

# 이름으로 넣기
"I ate {number} apples. so I was sick for {day} days.".format(number = 10, day = 3)
# 'I ate 10 apples. so I was for three days.'

# 인덱스와 이름을 혼용해서 넣기
"I ate {0} apples. so I was sick for {day} days.".format(10, day = 3)
# 'I ate 10 apples. so I was for three days.'

# 왼쪽 정렬
"{0:<10}".format("hi") # 'hi        '

# 오른쪽 정렬
"{0:>10}".format("hi") # '        hi'

# 가운데 정렬
"{0:^10}".format("hi") # '    hi    '

# 공백 채우기
"{0:=^10}".format("hi") # '====hi===='
"{0:!<10}".format("hi") # 'hi!!!!!!!!'

# 소수점 표현하기
y = 3.42134234
"{0:0.4f}".format(y) # '3.4213'
"{0:10.4f}".format(y) # '    3.4213'

# '{' 또는 '}' 문자 표현하기
"{{ and }}".format() # '{ and }'
