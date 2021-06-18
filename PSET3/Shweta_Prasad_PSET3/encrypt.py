'''
assume the existence of public_key.txt, plaintext.txt
output to a file named ciphertext.txt
'''

def modexp(m, e, n):
	"""
	This function computes modular exponentiation using
	the Square and Multiply algorithm. 
	"""
	r = 1
	while(e > 0):
		if (int(e)&1)==1: 
			r = r*m % n #multiply
		e = e/2
		m = m*m % n #square

	return r

#reading the public key
f = open("public_key.txt")
e, n = int(f.readline()), int(f.readline())

f.close()

#reading plaintext
plaintext = open("plaintext.txt").read()


l = []
for char in plaintext:
	c = modexp(ord(char), e, n)
	l.append(str(c))
f = open("ciphertext.txt", "w")
f.write(" ".join(l))
f.close()

print("\nFin encryption. The encrypted file is named ciphertext.txt\n")