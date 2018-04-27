import time
from threading import Thread, Lock

counter = 0
lock = Lock()


class Increment(Thread):
    def run(self):
        global counter

        lock.acquire()
        read_counter = counter
        print(f'Counter in {self.name} is {counter}')

        counter = read_counter + 1
        print(f'Counter in {self.name} after increment is {counter}')
        lock.release()


def use_increment(n_threads):
    threads = []
    for i in range(n_threads):
        t = Increment()
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f'Counter is {counter} and should\'ve been {n_threads}')


use_increment(100)


class CreateList(Thread):
    def __init__(self):
        super().__init__()
        self.entries = []

    def run(self):
        for i in range(10):
            time.sleep(1)
            self.entries.append(i)

        lock.acquire()
        print(self.entries)
        lock.release()


def use_create_list(n_threads):
    for i in range(n_threads):
        t = CreateList()
        t.start()


use_create_list(100)
