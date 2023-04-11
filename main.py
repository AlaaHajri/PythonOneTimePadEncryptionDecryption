import random

def msg_to_bin(txt):                                    #   msg_to_bin
    list1 = []                                          #   which is used to convert a text to a binary msg:                                         
    list2 = []
    list3 = []
    for i in range(len(msg)):
        list1.append(msg[i])                            #   We converted the msg to a list to separate the letters
        list2.append(ord(list1[i]))                     #   These letters in the list are converted to ASCII code
        list3.append(bin(list2[i])[2::].rjust(8,'0'))   #   Each ascii code is converted to a binary number
    # Un-comment to debug:
    print(list1)
    print(list2)
    print(list3)
    return list3

def bin_to_msg(txt):                                    #   "bin_to_msg" is the reverse of "msg_to_bin" 
    list1 = []                                          #   used to convert the binary code to a msg:
    list2 = []
    list3 = []
    for i in range(int(len(txt)/8)):
        list1.append(txt[8*i: 8*(i+1)])                 #   convert binair msg to 8 bit list
        list2.append(int(list1[i], 2))                  #   convert binary list to a number
        list3.append(chr(list2[i]))                     #   we will convert the numerical value to a character
    # Un-comment to debug:
    print(list1)
    print(list2)
    print(list3)
    return list3

def rand_key(p):                                        #   rand_key (After importing the "random" module)                   
    cle = ""                                            #   creates a random key with the same length of the binary               
    for i in range(p):                                  #   p = length of the key
        temp = str(random.randint(0, 1))                #   cle = is the key 
        cle += temp
    return (cle)

def one_time_pad_encrypt(plaintext, key):               #   encrypt the message with the binary key generated using the XOR
    ciphertext = ""
    for i in range(len(plaintext)):
        ciphertext += str(ord(plaintext[i]) ^ ord(key[i]))
    return ciphertext

def one_time_pad_decrypt(ciphertext, key):              #	encrypt the message with the binary key generated 
    plaintext = ""                                      #   using the XOR which is called one_time_pad_decrypt
    for i in range(len(ciphertext)):
        plaintext += str(ord(ciphertext[i]) ^ ord(key[i]))
    return plaintext

msg = "The message i want to encrypt"                               #   The encrypted message is saved in a "msg" variable
print("msg =",msg)

msgbinaire = msg_to_bin(msg)                                        #   We use msg_to_bin to convert the msg to a binary msg        
msgbinaire = ''.join(str(item) for item in msgbinaire)              #   binary msg without comma without bracket
print("msgbinaire:",msgbinaire,"de longuer", len(msgbinaire),"bit")

clebinaire = rand_key(len(msgbinaire))                              #   generate a random key with the same length of the binary message
print("clebinaire:",clebinaire,"de longuer", len(clebinaire),"bit")

msgchiffré = one_time_pad_encrypt(msgbinaire, clebinaire)           #   We use the one_time_pad_encrypt to encrypt the message
print("msgchiffré:",msgchiffré,"de longuer", len(msgchiffré),"bit")

mdechiffré = one_time_pad_decrypt(msgchiffré, clebinaire)           #   We decrypt the msg with the function one_time_pad_decrypt
print("mdechiffré:",mdechiffré,"de longuer", len(mdechiffré),"bit")

x = bin_to_msg(mdechiffré)
y = ''.join(map(str, x))
print(y)