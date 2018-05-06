# 입력 인수에 초깃값 미리 설정하기
def say_myself(name, old, man = True) :
    print('나의 이름은 %s입니다.' % name)
    print('나이는 %d살 입니다.' % old)
    if man :
        print('남자입니다.')
    else:
        print('여자입니다.')

say_myself('박응용', 27)
say_myself('박응용', 27, True)
say_myself('박응용', 27, False)

# 함수 입력 인수에 초기값을 설정할 때 주의할 사항
# def say_myself(name, man = True, old) :
#     print('나의 이름은 %s입니다.' % name)
#     print('나이는 %d살 입니다.' % old)
#     if man :
#         print('남자입니다.')
#     else:
#         print('여자입니다.')
#
# say_myself('박응용', 27)
# 초기화시키고 싶은 입력 변수들은 항상 뒤쪽에 위치
