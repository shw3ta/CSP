"""
For sufficiently small (n, e), we can take the following brute force 
approach: find the square root of n. This will be the uppoer bound 
for one of the factors. Loop through all odd numbers smaller than this 
square root. Find the number in this range such that n mod num = 0. 
This is one of the factors. 

Now it is trivial to find the other factor and calculate the private key from (n, e).
"""
import math

def find(n):
	sqrt = math.floor(math.sqrt(n))
	while (sqrt > 0):
		if n % sqrt == 0:
			return sqrt
		else:
			sqrt -= 2

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

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b % a, a)
    return (g, x - (b // a) * y, y)


def mod_inv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        print('modular inverse does not exist')

    inv = x % m
    return inv


n = int(input("Enter n: "))
e = int(input("Enter e: "))
p = find(n)
q = n // p
phi = (p - 1) * (q - 1)
d = mod_inv(e, phi)

print(f"The factors are p: {p} and q: {q}\n")
print(f"The private exponent is d: {d}\n")

choice = input("Do you want to commit forgery? Enter 'Y' or 'N'.\n")
if choice == 'N':
	print("Bye!")
else:
	m = int(input("Enter message: "))
	s = modexp(m, d, n)
	print(f"Here's the forged signature: {s}")