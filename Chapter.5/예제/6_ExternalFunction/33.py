# 스레드를 다루는 threading 모듈
import threading
import time

def say(msg) :
    while True :
        time.sleep(1)
        print(msg)

for msg in ['you', 'need', 'python'] :
    t = threading.Thread(target = say, args = (msg,))
    t.daemon = True
    t.start()

for i in range(100) :
    time.sleep(0.1)
    print(i)
