import threading
import time
import random

goods = 0
condition = threading.Condition()

def threadFun():
    global goods
    for i in range(10):
        condition.acquire()
        goods += 1
        condition.notify()
        condition.release()
        print("ThreadFun - %d" %goods)
        time.sleep(random.randrange(0,2))

class ThreadClass(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global goods
        for i in range(10):
            condition.acquire()
            goods -= 1
            condition.notify()
            condition.release()
            print("ThreadClass - %d" %goods)
            time.sleep(random.randrange(0,2))


if __name__ == "__main__":
    print("Waiting for subscriber to connect to {1} {0}".format("huang","ting"))
    key = '\x03'
    print(key)
    tFunc = threading.Thread(target = threadFun)
    tCls = ThreadClass()
    tFunc.start()
    tCls.start()
    tFunc.join()
    tCls.join()