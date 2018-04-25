# 문자열
"Life is too short, You need Python"
"a"
"123"

# 큰따옴표(")로 양쪽 둘러싸기
"Hello World"

# 작은따옴표(')로 양쪽 둘러싸기
'Python is fun'

# 큰따옴표 3개를 연속(""")으로 써서 양쪽 둘러싸기
"""Life is too short, You need python"""

# 작은따옴표 3개를 연속(''')으로 써서 양쪽 둘러싸기
'''Life is too short, You need python'''

# 문자열에 작은따옴표(')포함시키기
food = "Python's favorite food is perl"

# 문자열에 큰따옴표(")포함시키기
say = '"Python is very easy." he says.'

# \(백슬래시)를 이용해서 작은따옴표(')와 큰따옴표(")를 문자열에 포함시키기
food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\"he says."

# 여러 줄인 문자열을 변수에 대입하고 싶을 때
# 줄을 바꾸기 위한 이스케이프 코드 '\n' 삽입하기
multiline = "Life is too short\nYou need python"

# 연속된 작은 따옴표 3개(''') 또는 큰따옴표 3개(""")이용
multiline = '''
Life is too short
You need python
'''

multiline = """
Life is too short
You need python
"""

print(multiline)

# 문자열 더해서 연결하기
head = "Python"
tail = "is fun!"
head + tail

# 문자열 곱하기
a = "python"
a * 2

# multistring.py
print("=" * 50)
print("My Program")
print("=" * 50)

# 문자열 인덱싱
a = "Life is too short, You need Python"
a[3] # 'e'
a[0] # 'L'
a[12] # 's'
a[-1] # 'n'
a[-0] # 'L' a[0]와 같다
a[-2] # 'o' 뒤에서 두 번째 문자
a[-5] # 'y' 뒤에서 다섯 번째 문자

# 문자열 슬라이싱
a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3] # 'Life'
a[0:4] # 'Life'
a[0:3] # 'Lif'
a[0:5] # 'Life '
a[0:2] # 'Li'
a[5:7] # 'is'
a[12:17] # 'short'
a[19:] # 'You need Python'
a[:17] # 'Life is too short'
a[:] # 'Life is too short, You need Python'
a[19:-7] # 'You need'

a = "20010331Rainy"
data = a[:8] # 20010331
weather = a[8:] # Rainy
year = a[:4] # 2001
day = a[4:8] # 0331
weather = a[8:] # Rainy

# 문자열 포매팅
# 숫자 바로 대입
"I eat %d apples." % 3 # 'I eat 3 apples.'

# 문자열 바로 대입
"I eat %s apples." % "five" # 'I eat five apples.'

# 숫자 값을 나타내는 변수로 대입
number = 3
"I eat %d apples." % number # 'I eat 3 apples.'

# 2개 이상의 값 넣기
number = 10
day = "three"
"I ate %d apples, so I was sick for %s days." % (number, day)
# 'I ate 10 apples, so I was sick for three days.'

# 어떤 형태의 값이든 변환해 넣을 수 있는 %s 포맷 코드
"I have %s apples" % 3 # 'I have 3 apples'
"rate is %s" % 3.234 # 'rate is 3.234'

# 포맷 코드와 숫자 함께 사용하기
# 정렬과 공백
"%10s" % "hi" # '        hi'
"%-10sjane" % "hi" # hi        jane

# 소수점 표현하기
"%0.4f" % 3.42134234 # '3.4213'
"%10.4f" % 3.42134234 # '    3.4213'

# 문자 개수 세기
a = "hobby"
a.count('b') # 2

# 위치 알려주기 1
a = "Python is best choice"
a.find('b') # 10
a.find('k') # -1

# 위치 알려주기 2
a = "Life is too short"
a.index('t') # 8
# a.index('k')

# 문자열 삽입
a = ","
a.join('abcd') # 'a,b,c,d'

# 소문자를 대문자로 바꾸기
a = "hi"
a.upper() # 'HI'

# 대문자를 소문자로 바꾸기
a = "HI"
a.lower() # 'hi'

# 왼쪽 공백 지우기
a = " hi "
a.lstrip() # 'hi '

# 오른쪽 공백 지우기
a = " hi "
a.rstrip() # ' hi'

# 양쪽 공백 지우기
a = " hi "
a.strip() # 'hi'

# 문자열 바꾸기
a = "Life is too short"
a.replace("Life", "Your leg") # 'Your leg is too short'

# 문자열 나누기
a = "Life is too short"
a.split() # ['Life', 'is', 'too', 'short']
a = "a:b:c:d"
a.split(':') # ['a', 'b', 'c', 'd']
