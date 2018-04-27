import random
import time
from threading import Thread, RLock

items = []
lock = RLock()


class Producer(Thread):
    def run(self):
        global items

        while True:
            item = random.randint(0, 256)

            lock.acquire()
            items.append(item)
            print(f'Produced {item}')
            lock.release()

            time.sleep(random.random())


class Consumer(Thread):
    def run(self):
        global items

        while True:
            lock.acquire()
            item = items.pop(0)
            print(f'Consumed {item}')
            lock.release()

            time.sleep(random.random())


Producer().start()
Consumer().start()
