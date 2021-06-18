'''
for problem 1-2:
affine function used to encrypt is E(m) = c = 17x + 5 (mod 26)
thus, the decryption function is D(c) = x = 23(c - 5) (mod 26)

for problem 1-3:
the encryption function was found to be c = 3x + 5 (mod 26), thus
the decryption function is x = 9(c - 5) (mod 26)
'''
ciphertext2 = "NULNFSVIX"
ciphertext3 = "MRKNHYMFZHLEFIIMR"
plaintext = ""
choice = input("Enter 2 for problem 1-2.\nEnter 3 for problem 1-3.\n")

if choice == "3":
	print("\nCiphertext : " + ciphertext3)
	for c in ciphertext3:
		c = ord(c) #to ascii value
		m = (9 * (c - 5 - 65)) % 26 + 65 #in caps range
		m = chr(m) #back to character represented by ascii val
		plaintext = plaintext + m

if choice == "2":
	print("\nCiphertext : " + ciphertext2)
	for c in ciphertext2:
		c = ord(c)
		m = (23 * (c - 5 - 65)) % 26 + 65
		m = chr(m)
		plaintext = plaintext + m

print("Plaintext  : " + plaintext)
