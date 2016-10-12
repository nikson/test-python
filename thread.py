#!/usr/bin/python

import threading
import time

# version 2.7

class Worker(threading.Thread):
	def __init__(self, id, name, delay):
		threading.Thread.__init__(self)
		self.id = id
		self.name = name
		self.delay = delay

	def run(self):
		print "I am going to drive in...." + self.name
		DoWork(self.name, self.delay, 10)
		print "Kick out " + self.name

def DoWork(name, delay, loop):
	while loop:
		loop = loop - 1
		if loop < 0 : thread.exit()
		print "%s: %s" % (name, ' wating...') 
		time.sleep(delay);

if __name__ == "__main__":
	t1 = Worker(1, "t1", 5)
	t2 = Worker(2, "t2", 5)

	t1.start()
	t2.start()
	print("Exiting from main")
