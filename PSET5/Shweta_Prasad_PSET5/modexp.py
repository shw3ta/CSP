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

m = 123456789
e = 268812
n = 661643

res = modexp(m, e, n)
print(res)