#!/usr/local/bin/python

import sys

# command line argument processing 
if len(sys.argv) == 2 and sys.argv[1].isdigit():
        y = int(sys.argv[1])
        x = y // 2
        while x > 1: 
                if y % x == 0: 
                        print(y, 'has factor ', x)
                        break
                x -= 1
        else:
                print(y, 'is prime')
else:
        print('Invalid arguments')


# user define function 
def isprime(number):
        x = number // 2
        y = number
        while x > 1: 
                if y % x == 0: 
                        print(y, 'has factor ', x)
                        break
                x -= 1
        else:
                print(y, 'is prime')

        

