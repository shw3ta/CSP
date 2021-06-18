def egcd(a, b):
	if a == 0:
		print(f"({b}, {0}, {1})")
		return (b, 0, 1)

	g, y, x = egcd(b % a, a)
	print(f"({g}, {x - (b // a)}, {y})")
	return (g, x - (b // a) * y, y)

egcd(539, 1387)