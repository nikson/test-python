#!/usr/local/bin/python 

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
	
	def getData(self):
		return self.data

	def getNext(self):
		return self.next
	
	def setData(self, newdata):
		self.data = newdata
	
	def setNext(self, link):
		self.next = link
	
class LinkList(object):
	def __init__(self):
		self.root = None
	
	def add(self, item):
		node = Node(item)
		node.setNext(self.root)
		self.root = node
	
	def remove(self, data): 
		start = self.root
		ancestor = None
		while start.getNext() is not None and start.getData() != data:
			ancestor = start
			start = start.getNext()

		if ancestor is None:
			self.root = start.getNext()		# first data 
		else:
			ancestor.setNext(start.getNext())

	
	def search(self, data):
		start = self.root
		found = False 
		while start.getNext() is not None and not found:
			if  start.getData() == data:
				found = True
			else:
				start = start.getNext()

		return found

	def __str__(self):
		return self.__repr__()
	def __repr__(self):
		start = self.root
		nodes = [ start.getData() ]
		while start.getNext() is not None:
			start = start.getNext()
			nodes.append(start.getData())
		return ' -> '.join(nodes)

if __name__ == '__main__':
	print('Testing link list program')

	ll = LinkList()
	ll.add('e')
	ll.add('d')
	ll.add('c')
	ll.add('b')
	ll.add('a')
	print(ll)
	print(ll.search('d'))
	print(ll.search('k'))
	ll.remove('d')
	print(ll)
