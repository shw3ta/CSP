qpart = input("Enter 1 for part a, 2 for part b and so on. There are 5 parts.\n ")

if qpart == "1":
	cipher = "evire"

else:
	filename = input("enter filename: ")
	file = open(filename, "r")
	cipher = file.read()
	file.close()

for i in range(0, 26):
	plain=""
	for char in cipher:
		plain = plain + chr((ord(char) + i-97) % 26 + 97)
	print(" for rot "+ str(i) + " plaintext is: " + plain)