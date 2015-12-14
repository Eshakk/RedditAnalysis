#!/usr/bin/python

import threading
import time

class new_thread (threading.Thread):
    def __init__(self, threadName, delay):
        threading.Thread.__init__(self)
        self.tname = threadName
        self.delay = delay

    def run(self):
        print "Starting: " + self.tname + "time: " + time.ctime(time.time())
        tlock.acquire()
        print_time(self.tname, self.delay)
        tlock.release()
        print "Done: " + self.tname + "time: " + time.ctime(time.time())

def print_time(tname, delay):
    time.sleep(delay)
    print "%s: %s" % (tname, time.ctime(time.time()))

tlock = threading.Lock()
ts = []

thread1 = new_thread("t1", 2)
thread2 = new_thread("t2", 4)

ts.append(thread1)
ts.append(thread2)

for t in ts:
    t.start()

for t in ts:
    t.join()

print "Exiting main thread"

