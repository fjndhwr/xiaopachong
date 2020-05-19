from concurrent.futures import ThreadPoolExecutor
import threading


def get(a):
   # print(a)
    t = threading.currentThread()
    print(t.getName() + "\n")


if __name__ == '__main__':
    pool = ThreadPoolExecutor(10)
    for i in range(100):
        pool.submit(get, i)


