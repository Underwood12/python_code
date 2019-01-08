import multiprocessing
import time


def work_with(lock, f):
    with lock:
        fs = open(f, 'a+')
        n = 10
        while n > 1:
            fs.write('Locked acquired via with\n')
            n -= 1
        fs.close()


def work_no_with(lock, f):
    lock.acquire()
    try:
        fs = open(f, 'a+')
        n = 10
        while n > 1:
            fs.write('Lock acquired directly\n')
            n -= 1
        fs.close()
    finally:
        lock.release()


if __name__ == '__main__':
    lock = multiprocessing.Lock()
    f = 'file.txt'
    w = multiprocessing.Process(target=work_with, args=(lock, f))
    nw = multiprocessing.Process(target=work_no_with, args=(lock, f))
    w.start()
    nw.start()
    print('end')







