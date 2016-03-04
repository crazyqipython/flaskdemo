#!/usr/bin/python
class Queue():
	def __init__(self):
	    self.queue=[]
	def is_empty():
	    return self.queue==[]
	def push(self, item):
	    self.queue.insert(0, item)
	def dequeue(self):
	    return self.queue.pop()
	def size(self):
	    return len(self.queue)


if __name__ =='main':
    q=Queue()
    q.push('hello')
    q.push('dog')
    print q.queue
    q.push(3)
    q.dequeue()

	
	
	
