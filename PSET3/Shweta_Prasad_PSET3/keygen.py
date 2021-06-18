"""
must output public_key.txt, private_key.txt

submit the time it takes for keygen.py to execute. 

--------------------------------------------------

1. generate 2 large, distinct primes p and q ideally of similar byte length
2. multiply p and q; n = pq
3. find totient phi = (p-1)(q-1)
4. generate an e coprime to phi; (*)
5. find d using d.e equiv= 1 mod(phi) (*)


"""

import numpy as np
import random

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

def primality(p, security=200):

	u = 0
	r = p - 1

	if r%2 == 0:
		u = u + 1
		r = r>>1


	for i in range(security):

		a = random.randrange(2, p - 1)
		z = modexp(a, r, p)

		if (z != 1) and (z != (p - 1)):
			for j in range(1, u):
				z = modexp(z, 2, p)
				if z == 1: 
					return False

			if z != (p - 1):
				return False

	return True

def possible_randbits(length):

	p = random.getrandbits(length)

	p |= (1 << length - 1)
	p |= 1

	return p

def prime_gen(length=512):

	p = possible_randbits(length)

	while (True):
		
		if p&1 == 0:
			p = p | 1

		if primality(p) == False:
			p = possible_randbits(length)
		else:
			return p		



def gcd(a, b):
	"""
	This function computes the greatest common divisor 
	of integers a and b. 
	"""

	# ensuring that a > b
	if b > a:
		temp = a
		a = b
		b = temp

	if b == 0:
		return a
	else:
		return gcd(b, a % b)


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b % a, a)
    return (g, x - (b // a) * y, y)

# application of Extended Euclidean Algorithm to find a modular inverse
def mod_inv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        print('modular inverse does not exist')

    inv = x % m
    return inv

def e_gen(phi):

	print("\nGenerating the public key..\n")

	while (True):
		
		e = random.randrange(2, phi)
		if gcd(e, phi) == 1:
			return e
	
# --------------------------------------------------------
print("\nGenerating primes p and q.")
#p, q = 13, 11
#p, q = 7558766281268911182587030794705029989961567918343780352172253892335697791729267657809416033760239704847450433930330790220550776291910455206618756123371811, 6708648575351855678790400357100930965738175610609069832595809323726545894314850214898649663844358511169755584652603745525500560096324500655056923328227287 #do we generate the primes ourselves?
p, q = prime_gen(30), prime_gen(30)
n = p * q
print(p)
print(q)

phi = (p - 1) * (q - 1)
print("phi: ", phi)

#pick a random e from Zn such that it is coprime with n so that a mod inverse exists
e = e_gen(phi)

print("Generating the private key..\n")

d = mod_inv(e, phi)

print(f"checking for correct key set: {(int(e)*int(d)) % phi}")

# writing the public key in the required format
f = open("public_key.txt", "w+")
f.writelines([str(e), "\n", str(n)])
f.close()

# writing the private key in the required format
f = open("private_key.txt", "w+")
f.write(str(d))
f.close()

print("\nThe keys have been written to the files as specified.")