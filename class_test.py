#!/usr/local/bin/python

class Foo:
	# class method of python, 
	@classmethod
	def hello(cls):
		print('Hello from class method: %s' % cls.__name__)
	
	# instance method 
	def hello2(self):
		print('Hello from instance method: %s' % self.__class__.__name__)

	# static method, without acces to class and it's internal 
	@staticmethod 
	def hello3():
		print('Hello from static method: hello3')

	@property
	def val(self):
		return self._val

	@val.setter
	def val(self, v):
		self._val = v

	@val.deleter
	def val(self):
		del self._val

	def __init__(self):
		self._val = None 
        
class Bar(Foo):
	#def __init__(self): pass
		#super().hello2()
	def hello2(self):
		print('hello from bar')

class Car(Foo):
	def hello2(self):
		print('hello from car')
        
# Diamond inheritance problem, DFS-Left-to-right
class Dar( Bar,  Car):
	pass

if __name__== '__main__':
	Foo.hello()
	Foo().hello()

	Foo().hello2()

	Foo().hello3()
	f = Foo()
	f.val = 100
	print(f.val)
	Bar()
	Dar().hello2()
