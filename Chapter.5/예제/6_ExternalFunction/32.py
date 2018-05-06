# calendar
import calendar

# 그 해 전체 달력
print(calendar.calendar(2015))
calendar.prcal(2015)

# 한 달의 달력
calendar.prmonth(2015, 12)

# 요일 정보 반환
print(calendar.weekday(2015, 12, 31))

# 1일의 요일, 그 달이 며칠까지 있는지 반환
print(calendar.monthrange(2015, 12))

# random
import random

# 0.0에서 1.0 사이의 실수 중에서 난수값을 리턴하는 함수
print(random.random())

# 1에서 10 사이의 정수 중에서 난수값을 리턴하는 함수
print(random.randint(1, 10))

# 1에서 55 사이의 정수 중에서 난수값을 리턴하는 함수
print(random.randint(1, 55))

# random_pop.py
# pop 메서드에 의해 꺼내진 요소는 삭제된다.
def random_pop(data) :
    number = random.randint(0, len(data) - 1)
    return data.pop(number)

if __name__ == '__main__' :
    data = [1, 2, 3, 4, 5]
    while data : print(random_pop(data))

# choice 함수는 입력으로 받은 리스트에서 무작위로 하나를 선택하여 리턴
def random_pop(data) :
    number = random.choice(data)
    data.remove(number)
    return number

# 리스트의 항목을 무작위로 섞고 싶을 때
data = [1, 2, 3, 4, 5]
random.shuffle(data)
print(data)

# webbrowser
import webbrowser

# 기본 웹브라우저가 자동으로 실행되게 하는 함수
webbrowser.open('http://google.com')

# 이미 브라우저가 실행된 상태에서도 새로운 창으로 열리도록 하는 함수
webbrowser.open_new('http://google.com')
