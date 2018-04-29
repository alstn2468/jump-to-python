'''
오른쪽과 같이 총 10줄로 이루어진 sample.txt 파일이 있다.
다음 쪽을 보며, sample.txt 파일의 숫자값을 모두 읽어
총합과 평균값을 구한 후 평균값을 result.txt라는
파일에 쓰는 프로그램을 작성해보자.

sample.txt
70
60
55
75
95
90
80
80
85
100
'''

f = open('sample.txt', 'r')
lines = f.readlines()
f.close()

total = 0
for line in lines :
    score = int(line)
    total += score

average = total/len(lines)

f = open('result.txt', 'w')
f.write(str(average))
f.close()
