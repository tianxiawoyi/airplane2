import threading
import time
import os

g_nums = [11,22]
g_ss = 33
def test1(tem1,tem2):
    tem1.append(33)
    print("----test1----->%s" % str(tem1))
    print("----test1----->%s" % str(tem2))
    print("----test1name----->%s" % str(threading.current_thread().getName()))
    print("----test1name----->%s" % str(threading.currentThread().getName()))



def test2(tem1,tem2):
    print("------test2--->%s" % str(tem1))
    print("------test2--->%s" % str(tem2))


def main():

    t1 = threading.Thread(target=test1,args=(g_nums,g_ss),name="t1")
    t2 = threading.Thread(target=test2,args=(g_nums,g_ss))
    t1.start()
    time.sleep(1)

    t2.start()
    time.sleep(1)
    print("----main----->%s" % str(g_nums))


lock = threading.Lock()
lock.acquire(timeout= 10)      # 设置超时时间防止死锁

if __name__ == '__main__':
    main()