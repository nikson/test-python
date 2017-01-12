#!/usr/local/bin/python

def func(arr):
	data =list(arr)
	rows =  0
	cols = len(data[0]) if len(data) > 0 else 0
	r = 0
	print(cols)
	while rows < len(data) and cols > 0:
		if data[rows][cols-1] < 0:
			r += cols
			rows = rows + 1
		else:
			cols = cols - 1
	return r

if __name__ == '__main__':
	n = [ [ -3, -2, -1, 1], [-2, -1, 0, 2], [1, 2, 3, 4] ]
	print(func(n))

