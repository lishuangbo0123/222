# 李双博
# 学习python
# 开发时间 2021/12/24  1:44
from threading import Thread  #多线程
from multiprocessing import Process #多进程
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor #线程池和进程池

class MyThread(Thread):
    def run(self) -> None:
        for i in range(1000):
            print('子线程', i)

def func():
    for i in range(1000):
        print('子线程',i)
def fn(name):
    for i in range(100):
        print(name,i)

if __name__ == '__main__':
    #通过直接创建线程的方式开辟新线程
    t = Thread(target=func,args=('周杰伦',))  #传参必须是元组
    t.start() #这里只是告诉线程可以开始工作了，但是什么时候执行是由CPU决定的
    #通过创建线程类来创建线程
    thread = MyThread()
    thread.start()

    #创建进程
    p = Process(target=func,args = ('周杰',))  #语法和创建线程一样
    p.start()

    for i in range(1000):
        print('主线程',i)

    #线程池
    with ThreadPoolExecutor(50) as t:#开辟50条线程
        for i in range(100):    #假设有100个任务
            t.submit(fn,name = 'aaa')

    print('over')