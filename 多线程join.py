import threading
import time

def thread_job():
    print('T1 start\n')
    for i in range(10):
        time.sleep(0.1)
    print('T1 finish\n')

def T2_job():
    print('T2 start\n')
    print('T2 finish\n')

def main():
    added_thread = threading.Thread(target=thread_job, name='T1')
    print('11111111111:')
    thread2 = threading.Thread(target=T2_job, name='T2')
    print('2222222222:')
    added_thread.start()
    print('333333333333:')
    time.sleep(20)
    thread2.start()
    print('444444444444444:')
    # added_thread.join()
    # thread2.join()
    print('all done\n')
    print('55555555555555555')


if __name__ == '__main__':
    main()