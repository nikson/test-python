#!/usr/local/bin/python

import sys
import math

def isprime(num):
	if num == 1 or num%2== 0 and num != 2 : return False
	#elif num == 2: return True
	else:
		for x in range(3, int(math.sqrt(num))):
			if num%x == 0:
				return False
	return True
	

if __name__ == '__main__':
	#print(sys.argv)
	nums = sys.argv[1:]
	ret = list(map(isprime, map(int, nums)))
	print(ret)
