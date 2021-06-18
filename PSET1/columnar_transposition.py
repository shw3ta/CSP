
def getOrderedKey(k):

	"""
	Description : 	function that returns the  alphabetically ordered position
					of characters in the key string
	Input		:	the key 'k' (string)
	Output		: 	the list of indices 'orderedKey', but alphabetically or-
					-dered (list)
	"""
	orderedKey = []
	for idx, char in enumerate(k):
		pos = 1 # position when alphabetically ordered
		prefix = k[ : idx]

		for i, ch in enumerate(prefix):
			if ch > char:
				# to give alphabets closer to Z higher positional value
				# here, an updation is done every time a new character in the key 
				# string is encountered
				orderedKey[i] = orderedKey[i] + 1
			else:
				pos = pos + 1

		orderedKey.append(pos)

	return orderedKey

#---------------------------------------------------------------------------------------#

def encrypt(p, k):
  """
  Description	:	function to encrypt given plaintext with chosen key
  Input			: 	plaintext 'p' (string), key 'k' (string)
  Output		:	returns encrypted plaintext 'c' (string)

  """
  row, col = 0, 0
  table = [[]]
  c = ""

  orderedKey = getOrderedKey(k)

  # filling up a table row by row with plaintext chars
  for idx, char in enumerate(p):
    table[row].append(char)
    col = col + 1
    if col >= len(k): # move to next row
      col = 0
      row = row + 1
      table.append([]) # make way for the new row
    

  # do the alphabetical switcheroo while appending
  for i in range(len(k)):
    newpos = orderedKey.index(i + 1) #numbered from 1
    for row in range(len(table)):
      if len(table[row]) > newpos:
        c = c + table[row][newpos]


  return c   

 #--------------------------------------------------------------------------------------#

def decrypt(c, k):
	"""
	Description 	: function to decrypt given ciphertext with given key
	Input			: ciphertext 'c' (string), key 'k' (string)
	Output			: returns decrypted message 'p' (string)


	"""
  
  p = ""
  orderedKey = getOrderedKey(k)
   

  # now to make the table
  n_cols = len(k)
  n_rows = len(c)//n_cols # integer division

  # to ensure that there is enough space in the table
  # in this house, we are inclusive
  if n_cols * n_rows < len(c): n_rows = n_rows + 1 

  table = []
  ctr = 0

  # empty table initialized with '' in place only where there should be chars
  for row in range(n_rows):
    table.append([])
    for col in range(n_cols):
      if ctr < len(c):
        table[row].append('')
        ctr = ctr + 1

  
  # filling up the table for decryption
  pos = 0
  for i in range(len(k)):
  	# finding the appropriate column to fill
  	# col will store the index of the position i, in the key after alphabetical numbering
    col = orderedKey.index(i + 1)

    row = 0
    while (row < n_rows) and (len(table[row]) > col):
      table[row][col] = c[pos] # fill appropriate character from ciphertext into cell
      row, pos = row + 1, pos + 1 # updation

  # let the appending begin
  for row in range(n_rows):
    for col in range(len(table[row])):
      p = p + table[row][col]
  
  return p

#---------------------------------------------------------------------------------------#
  

f = open("columnar_ciphertext.txt", "r")
c = f.read()
f.close()

f = open("columnar_key.txt", "r")
k = f.read().splitlines()[1] #just the key for me, please
f.close()

p = decrypt(c, k)

f = open("columnar_plaintext.txt", "w")
f.write(p)
f.close()