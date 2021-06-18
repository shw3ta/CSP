import numpy as np

def gcd(a, b):
	"""
	This function computes the greatest common divisor 
	of integers a and b. 
	"""
	if b == 0:
		return a
	else:
		return gcd(b, a % b)

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


def factor(n, e, d):
	"""
	finds s, t such that ed - 1 = (2^s)*t and t is odd	"""

	s = 0
	t = e * d - 1

	Z = np.arange(1, n, dtype = np.int64)
	
	gcds = []
	to_delete = []

	for i in range(len(Z)):
		g = gcd(Z[i], n)
		gcds.append(g)

	for i in range(len(Z)):
		if gcds[i] != 1:
			to_delete.append(i)
	Zstar = np.delete(Z, to_delete)
	
	while (t%2 == 0):
		s = s + 1
		t = t/2

	while (True):
		a = np.random.choice(Zstar) #choose from Zn*
		b = modexp(a, t, n)
		while (modexp(b, 2, n) != 1):
			b = modexp(b, 2, n)

		if b%n != 1 or b%n != -1:
			break;

	p = gcd(b - 1, n)
	q = n//p
	return (p, q)

# finding the factors
while (True):
	p, q = factor(1501, 323, 539)

	if p != 1 and q != 1:
		break


n = p * q
phi = (p - 1) * (q - 1)
confirm = 323 * 539 % phi

print(f"The factors discovered are p = {p} and q = {q}")
print(f"e.d mod totient =  {confirm}")