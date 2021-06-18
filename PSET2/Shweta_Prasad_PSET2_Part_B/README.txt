This is an attempt to implement the Data Encryption Standard. 
The Initial and Final Permutations have not been implemented. 
File manipulation may throw up some occasional errors, thanks to cpp and Barun Parruck. 
Anticipatory apologies for what you may find in here. 

Padding: PKCS5
Chaning Mode: CBC

------------------------------------------------------------------------------------------------------------------

Make sure to put the files 'plaintext.txt', 'key.txt', 'ciphertext.txt' in the same directory as this program file. 

To compile the program, open terminal and run the following commands in the respective directory:
 g++ -o des des.cpp
 ./des

After these 2 instructions are run, you will be prompted to enter 'E' to encrypt and 'D' to decrypt.
Once the mode is chosen, you will be updated on whether or not the appropriate files can be found in the same directory. 

You will be prompted to enter 'y' for yes or 'n' for no, if you want to/ do not want to enter a custom Initialization Vector. After this, you will be prompted to enter the IV. 

Then the program will update you on completion and terminate. The answers can be found in the appropriate txt files. 

Note: you can run the modes separately as long as the appropriately named files are used. However, due to some file manipulations that gave a host of trouble, it would be best to use the file that is output by the Encrypt function as input to the Decrypt function and vice-versa. 

------------------------------------------------------------------------------------------------------------------