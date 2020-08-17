from concurrent.futures import ThreadPoolExecutor
import threading
import time


def get(a):
   # print(a)
    t = threading.currentThread()
    print(t.getName() + "\n")
    time.sleep(1)


def ab():
    a = "sdasdasds1d2as4dsa5dweqwyhyg"
    b = "123456"
    print(a ^ b)


if __name__ == '__main__':
    pool = ThreadPoolExecutor(64)
    set = pool._threads
    for i in range(100):
        pool.submit(get, i)
    for t in set:
        t.join()  # 阻塞主进程，进行完所有线程后再运行主进程
    print("11111")


