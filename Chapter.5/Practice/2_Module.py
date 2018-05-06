'''
이전 문제에서 작성한 Calculator 클래스를 calculator.py라는
파일로 저장하자. 그리고 이 파일을 모듈로 사용하려고 한다.
다음처럼 동작하도록 만들어보자.
>>> from calculator import Calculator
>>> cal1 = Calculator([1, 2, 3, 4, 5])
>>> cal1.sum()
15
'''

from calculator import Calculator

cal1 = Calculator([1, 2, 3, 4, 5])
print(cal1.sum()) # 15
