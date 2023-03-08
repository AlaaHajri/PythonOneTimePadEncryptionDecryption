########################################################################################################################
# 1)	Le message a chiffré est sauvegardé dans une variable « msg »
msg = "je suis en cours"
print("msg =",msg)
############ 2)	On a créé une fonction qui s’appelle « msg_to_bin » qui sert a convertir un texte vers un msg binaire
def msg_to_bin(txt):
    list1 = []
    list2 = []
    list3 = []
    for i in range(len(msg)):
        list1.append(msg[i])                           #3)	On a convertie le msg vers une liste pour séparer les lettres
        list2.append(ord(list1[i]))                    #4)	Ces lettres dans la liste sont converties vers le code ASCII
        list3.append(bin(list2[i])[2::].rjust(8,'0'))  #5)	Chaque code ascii est convertie vers un nombre binaire
    print(list1)
    print(list2)
    print(list3)
    return list3


msgbinaire = msg_to_bin(msg)  # 6)	On utilise la fonction msg_to_bin pour convertir le msg vers un msg binaire
msgbinaire = ''.join(str(item) for item in msgbinaire) # msg binaire sans virgule sans croché
print("msgbinaire:",msgbinaire,"de longuer", len(msgbinaire),"bit")

########################################################################################################################
# 7)	On va générer une clé aléatoire avec la même longueur du message binaire
import random
def rand_key(p):                #8)	Après avoir importé le module « random », on a crée une nouvelle fonction message
    cle = ""                    #  qui sert a crée une clé aléatoire avec la même longueur du binaire
    for i in range(p):                      # p = longeur de la cle
        temp = str(random.randint(0, 1))    # cle = est la clé
        cle += temp

    return (cle)

clebinaire = rand_key(len(msgbinaire))
print("clebinaire:",clebinaire,"de longuer", len(clebinaire),"bit")
########################################################################################################################
#9)	On vas crée un module qui sert a encrypter le message avec la clé binaire générer en utilisant l’XOR
def one_time_pad_encrypt(plaintext, key):
    ciphertext = ""
    for i in range(len(plaintext)):
        ciphertext += str(ord(plaintext[i]) ^ ord(key[i]))
    return ciphertext

# 10)	 On utilise la fonction one_tiome_pad_encrypt pour crypter le message
msgchiffré = one_time_pad_encrypt(msgbinaire, clebinaire)
# msgchiffré = ''.join(str(item) for item in l) #pour supprimer les crochers et les virgules entre les bits
print("msgchiffré:",msgchiffré,"de longuer", len(msgchiffré),"bit")
########################################################################################################################
# 11)	On va créer un module qui sert à cryper le message avec la clé binaire générer en utilisant l’XOR qui s’appelle one_time_pad_decrypt
def one_time_pad_decrypt(ciphertext, key):
    plaintext = ""
    for i in range(len(ciphertext)):
        plaintext += str(ord(ciphertext[i]) ^ ord(key[i]))
    return plaintext

# 12)	On décrypte le msg avec la fonction one_time_pad_decrypt
mdechiffré = one_time_pad_decrypt(msgchiffré, clebinaire)
# msgchiffré = ''.join(str(item) for item in l) #pour supprimer les crochers et les virgules entre les bits
print("mdechiffré:",mdechiffré,"de longuer", len(mdechiffré),"bit")
########################################################################################################################
# 13)	 On a créé une nouvelle fonction qui fais l’inverse de l’étape 6 qui s’appelle bin_to_msg qui sert à convertir le code binaire vers un msg
def bin_to_msg(txt):
    list1 = []
    list2 = []
    list3 = []
    list_to_str =''

    for i in range(int(len(txt)/8)):
        list1.append(txt[8*i: 8*(i+1)]) #   convertir le msg binair vers une list de 8 bit
        list2.append(int(list1[i], 2))  #   convertir la list binaire vers un numero
        list3.append(chr(list2[i]))     #   on vas convertir la valeur numérique vers un character

    print(list1)
    print(list2)
    print(list3)
    return list3

x = bin_to_msg(mdechiffré)
y = ''.join(map(str, x))
print(y)