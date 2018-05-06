# pickle
# 객체의 형태를 유지하면서 파일에 저장하는 함수
import pickle
f = open('test.txt', 'wb')
data = {1 : 'python', 2 : 'you need'}
pickle.dump(data, f)
f.close()

# 객체의 형태를 유지하면서 파일에서 불러오는 함수
f = open('test.txt', 'rb')
data = pickle.load(f)
print(data) # {1: 'python', 2: 'you need'}
