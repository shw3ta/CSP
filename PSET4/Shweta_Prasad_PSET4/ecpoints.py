from math import sqrt, floor

def params():

	while (True):
		a = int(input("Enter a: "))
		b = int(input("Enter b: "))
		p = int(input("Enter p: "))

		check = 0

		if p%2 != 0:
			check = (4 * a**3 + 27 * b**2) % p

		if check != 0:
			print(f"\nThe elliptic curve entered is:\ny^2 = x^3 + {a}x + {b} mod {p}.\n")
			return a, b, p

		else:
			print("\nThe given set of parameters do not guarantee a non-singular curve. Enter again:\n")

def possible_point(a, b, p):

	x = 0
	points = []
	points_nonzero_y = []
	while (True):
		t =  x**3 + a*x + b
		#print(f"t mod p =>  {t} mod {p}")
		y = sqrt(t % p)
		#print(f"x: {x}, y: {y}\n")
		if y == floor(y) :
			# y is an integer
			points.append((x, floor(y)))
			if y != 0:
				points_nonzero_y.append((x, floor(y)))
		
		x = x + 1

		if x > 100:
			return points, points_nonzero_y


a, b, p = params()
points, points_nonzero_y = possible_point(a, b, p)


if points_nonzero_y == []:
	print("\nSorry! No valid point such that the y coordinate is non-zero could be found under x <= 100. No point in this EC can be doubled.\n")
else:
	print("\nThe points that can be doubled are:\n")
	print(points_nonzero_y)
	
	print("\nThe list of all points on the EC with x coordinate <= 100 are: \n")
	print(points)