#!/usr/local/bin/python

def subset_sum(s, k, r, found = False):
	x[k] = 1
	if s + w[k] == m:
		found = True
		print('subset sum found')
		display(x)
		return found
	elif s+w[k]+w[k+1] <=m:
		subset_sum(s+w[k], k+1, r-w[k])
	if s+r-w[k] >= m and s+w[k+1] <= m:
		x[k] = 0
		subset_sum(s, k+1, r-w[k])
	return found

def display(ss):
	for idx,val in enumerate(ss):
		if val == 1:
			print(w[idx])


if __name__ == '__main__':
	global m 
	global w
	global x

	w = [ 5, 10, 12, 13, 17]
	m = 30 
	x = [0] * len(w)
	total = sum(w)
	subset_sum(0, 0, total)
