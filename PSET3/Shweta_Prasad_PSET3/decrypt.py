'''
assume the existence of ciphertext.txt,  public_key.txt, private_key.txt
output to a file named deciphertext.txt
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

#reading the private key
f = open("private_key.txt")
d = int(f.readline())


#obtaining n from the public key file
f = open("public_key.txt")
n = int(f.readlines()[1])

f.close()

#reading ciphertext
# ciphertext = open("ciphertext.txt").read()
# print(ciphertext)
ciphertext = open("ciphertext.txt").read()

l = ciphertext.split(" ")

f = open("deciphertext.txt", "w+")

plaintext = []

for thing in l:
	print("Thing: :",thing)
	char = int(thing)
	de = modexp(char, d, n)
	print("de: ", de)
	
	plaintext.append(chr(de))
	
plaintext = ''.join(plaintext)
f.write(plaintext)

print("\nFin decryption. Find the deciphered output in deciphertext.txt\n")	





#calculating the decryption
# deciphertext = ""

# for i in ciphertext:
# 	c = modexp(ord(i), d, n)
# 	deciphertext+=chr(c)

# print(f"deciphertext : {deciphertext}")

# #writing to file
# f = open("deciphertext.txt", "w+")
# f.write(str(deciphertext))
# f.close()