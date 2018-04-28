'''
while문을 이용하여 아래와 같이 별(*)을 표시하는 프로그램을 작성해 보자.
*
**
***
****
*****
'''

i = 0

while True :
    i += 1
    if i > 5 : break
    print('*' * i)
