#!/usr/local/bin/python

# Always operate on raw bytes, never on encoded strings. 
# Only use hex and base64 for pretty-printing.
# OTP: c = m xor k, m = c xor k

def XOR(M, K):
	m_bin = hex2bin(M)
	k_bin = hex2bin(K)
	data_bin = ''.join([ str(int(a,2) ^ int(b,2)) for (a,b) in zip(m_bin, k_bin)])
	data_hex = bin2hex(data_bin, 4)
	return data_hex

def getkey(M, C):
	# Convert hex string to binary then XOR to get the key
	m_bin = hex2bin(M)
	c_bin = hex2bin(C)
	key_bin = ''.join([ str(int(a,2) ^ int(b,2)) for (a,b) in zip(m_bin, c_bin)])
	key = bin2hex(key_bin, 4)
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
	m2 = 'attach at dusk'
	c1 = '09e1c5f70a65ac519458e7e53f36'
	m1_hex = m1.encode().hex()
	# Get key from message and cipher (M xor C)
	key = getkey(m1_hex, c1)	
	print('Key:' ,key)
	print()
	# Decrypt message 1 from cipher 
	data = XOR(c1, key)
	print('Decrypt message:' , bytes.fromhex(data))
	print()	
	# Encrypt message 2	
	m2_hex = m2.encode().hex()
	c2 = XOR(m2_hex, key)
	print('Encrypt message:' , c2)
	