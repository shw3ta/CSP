# looks like there is a problem in the frequency analysis section. 

def splitAndStoreBy(c, l):
	""" takes ciphertext and key length of choice (manual);
		return 'blob', a list with appropriately split characters
	"""

	# initialize
	blob = []
	for i in range(l):
		blob.append("")

	# fill
	for idx, char in enumerate(c):
		i = idx % l
		blob[i]= blob[i] + char

	return blob


def etTuBrute(s, top_n = 4):
	""" takes a substring off the 'blob' and does bruteforce Ceasar on it. 
		then for each 26 decryptions, counts the fq of each alphabet and 
		compares it with ELF, puts dissimilarity in a table.
		returns a list of top 4 most likely shift vals

		dissimilarity is basic sum of chi square vals
	"""
	s = s.upper()

	# english letter frequency, ironically from the language in use and not the dictionary
	ELF = {	'E':  12.49, 'T':   9.28, 'A':   8.04, 'O':   7.64, 'I':   7.57, 'N':   7.23, 
			'S':   6.51, 'R':   6.28, 'H':   5.05, 'L':   4.07, 'D':   3.82, 'C':   3.34,
			'U':   2.73, 'M':   2.51, 'F':   2.40, 'P':   2.14, 'G':   1.87, 'W':   1.68,
			'Y':   1.66, 'B':   1.48, 'V':   1.05, 'K':   0.54, 'X':   0.23, 'J':   0.16,
			'Q':   0.12, 'Z':   0.09
		}

	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	table = []
	for i in range(26):
		plain = ""
		for char in s:
			plain = plain + chr((ord(char) + i - 65) % 26 + 65)

		ctr = {} #fq counter; not yet in percent
		for char in plain:
			if char in ctr:
				ctr[char] += 1
			else:
				ctr[char] = 1



		dissimilarity = 0 # to implement chi square later
		for letter in alphabet:
			if (letter in ctr) :
				val = ctr[letter]/len(plain) * 100

				e_val = len(plain) * ELF[letter] / 100
				chisq = ((val - e_val)**2)/e_val
				dissimilarity = dissimilarity + chisq

		table.append([dissimilarity, i])
	

	table.sort()
	

	shiftvals = []
	for i in range(top_n):
		shiftvals.append(alphabet[table[i][1]]) #appending chars directly

	print(shiftvals)

	return shiftvals


def possibleKeys(l, masterlist):
	"""	masterlist will have the respective top 4 (by default) possibilities 
		for each position  in the key of length l that we are trying to find
		assuming that masterlist is a list of lists of chars

		this function will permute all of those options for each position and 
		return a list of keys

		this function helps shorten the search space vastly
	"""

	biglist = []
	if l == 3:
		for c1 in masterlist[0]:
			key = c1
			for c2 in masterlist[1]:
				key1 = key + c2
				for c3 in masterlist[2]:
					key2 = key1 + c3
					biglist.append(key2)


	if l == 4:
		for c1 in masterlist[0]:
			key = c1
			for c2 in masterlist[1]:
				key1 = key + c2
				for c3 in masterlist[2]:
					key2 = key1 + c3
					for c4 in masterlist[3]:
						key3 = key2 + c4
						biglist.append(key3)


	if l == 5:
		for c1 in masterlist[0]:
			key = c1
			for c2 in masterlist[1]:
				key1 = key + c2
				for c3 in masterlist[2]:
					key2 = key1 + c3
					for c4 in masterlist[3]:
						key3 = key2 + c4
						for c5 in masterlist[4]:
							key4 = key3 + c5
							biglist.append(key4)

	if l == 6:
		for c1 in masterlist[0]:
			key = c1
			for c2 in masterlist[1]:
				key1 = key + c2
				for c3 in masterlist[2]:
					key2 = key1 + c3
					for c4 in masterlist[3]:
						key3 = key2 + c4
						for c5 in masterlist[4]:
							key4 = key3 + c5
							for c6 in masterlist[5]:
								key5 = key4 + c6
								biglist.append(key5)


	return biglist


def decrypt(c, k):
	""" takes the ciphertext string and key string as input, both in caps.
		returns decrypted message
	"""
	p = ""
	translate = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for idx,char in enumerate(c):

		subkey = k[idx % len(k)]
		i = translate.index(subkey)
		p = p + chr((ord(char) + i - 65) % 26 + 65)


	return p





fname = input("Enter filename: ")
f = open(fname, "r")
c = f.read()
f.close()

l = int(input("Enter your guess for the key length: "))
print("You entered : " + str(l) + "\n")

split_c = splitAndStoreBy(c, l) # a list of strings

#getting and appending shiftvals
masterlist = []
for i in range(l):
	shiftvals = etTuBrute(split_c[i], top_n = 5)
	masterlist.append(shiftvals)

print(masterlist)

keylist = possibleKeys(l, masterlist)
#print(keylist)
fname , fname_k= input(" Enter the name of the file you want to store your output in: "), input(" Enter the name of the file for the key: ")

f = open(fname, "w+")
f_= open(fname_k, "w+")
for k in keylist:
	p = decrypt(c.upper(), k)
	f.write(f"Key : {k} \n Key index : {keylist.index(k)} \n Plaintext : {p} \n")
	f_.write(f"Key : {k} \n Key index : {keylist.index(k)} \n")