# 예외 처리
# try, except 문
try :
    4 / 0
except ZeroDivisionError as e :
    print(e)

# try .. else
try :
    f = open('foo.txt', 'r')
except FileNotFoundError as e :
    print(str(e))
else :
    data = f.read()
    f.close()

# try .. finally
f = open('foo.txt', 'r')
try :
    # 무엇을 실행한다.
finally :
    f.close()
