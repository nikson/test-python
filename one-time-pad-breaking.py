#!/usr/local/bin/python

# Always operate on raw bytes, never on encoded strings. 
# Only use hex and base64 for pretty-printing.
# OTP: c = m xor k, m = c xor k

def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def XOR(M, K):	
	data = "".join([ chr(ord(a) ^ ord(b)) for (a,b) in zip(M, K)])
	return data

def getkey(M, C):
	key = "".join([ chr(ord(a) ^ ord(b)) for (a,b) in zip(M,C)])	
	return key
	
def bin2hex(bin, pad):
	# convert bin to int then hex, [2:] - exclude hex identifier 
	data = ''.join(hex(int(bin[i:i+pad], 2))[2:] for i in range(0,len(bin),pad))
	return data
	
def hex2bin(hex):
	bin = ''.join('{0:04b}'.format(int(x,16)) for x in hex)
	return bin

if __name__ == "__main__":
	m1 = 'attack at dawn'
	m2 = 'attack at dusk'
	c1 = '09e1c5f70a65ac519458e7e53f36'
	m1_hex = m1.encode().hex()
	# Get key from message and cipher (M xor C)
	key = getkey(m1_hex, c1)
	print('Key:' , key.encode().hex())
	print()
	# Decrypt message 1 from cipher 
	data = XOR(c1, key)
	print('Decrypt message:' , bytes.fromhex(data))
	print()	
	# Encrypt message 2	
	m2_hex = m2.encode().hex()
	c2 = XOR(m2_hex, key)
	print('Encrypt message:' , c2)
	