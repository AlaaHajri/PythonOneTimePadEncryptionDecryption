# PythonOneTimePadEncryptionDecryption
 PythonOneTimePadEncryptionDecryption
This script contains Python code for encrypting and decrypting a message using a one-time pad encryption technique. The script works as follows:

A message to be encrypted is stored in a variable called "msg" and printed.
A function called "msg_to_bin" is defined to convert the message into a binary message.
The function converts the message into a list to separate the letters.
The letters in the list are converted into ASCII code.
Each ASCII code is converted into a binary number.
The "msg_to_bin" function is used to convert the message into a binary message, which is then joined together to form a single binary string.
A random key with the same length as the binary message is generated using the "random" module.
A function called "rand_key" is defined to create the random key.
A module is created to encrypt the message using the XOR operation with the random key.
The "one_time_pad_encrypt" function is used to encrypt the message.
A module is created to decrypt the message using the XOR operation with the random key.
The "one_time_pad_decrypt" function is used to decrypt the message.
A new function called "bin_to_msg" is created to convert the binary message back into text.
The decrypted message is passed to the "bin_to_msg" function to convert it back to text and print it.
Overall, the script uses the one-time pad encryption technique to encrypt and decrypt a message. The technique uses a random key that is used only once to encrypt the message, making it difficult to crack.