import numpy as np
import base64
import extendedvigenere as ev

def cipher64(hex):
    c64 = base64.b64encode(bytes.fromhex(hex)).decode()
    return(c64)

def ksa(k):
    s = [i for i in range (256)] 
    j = 0
    for i in range (256):
        j = ((j+ s[i] + k[i % len(k)]) % 256)
        
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
    return s

def prga(s, n):
    i = 0
    j = 0
    stream = []

    while n>0:
        i = (i + 1) % 256
        j = (j + s[i]) % 256

        temp = s[i]
        s[i] = s[j]
        s[j] = temp

        t = (s[i] + s[j]) % 256
        u = (ord(ev.extvigenereencrypt(chr(s[t]),chr((t*s[i]) % 256))) % 256)
        stream.append(u)
        n-=1
    return stream

def keyprep(sk):
    return([ord(c)for c in sk])

def enkripRC4(key,text):
    key = keyprep(key)
    S = ksa(key)
    keystream = np.array(prga(S, len(text)))
    plaintext = np.array([ord(c) for c in text])
    cipher = keystream ^ plaintext
    return cipher

def cipherhex(cipher):
    return (cipher.astype(np.uint8).data.hex())

def ciphertext(cipher):
    text = "".join(chr(c)for c in cipher)
    return (text)
    
# #--main--    
# # --enkripsi--
# key = input("enter key : ")
# text = input("enter text : ")
# cipher = enkripRC4(key,text)
# hex = cipherhex(cipher)
# ctext = ciphertext(cipher)
# c64 = cipher64(hex)
# print("Cipher : ",cipher)
# print("Cipher hex :",hex)
# print("Cipher str : ",ctext)
# print("Cipher Base 64 : ",c64)

# # --dekripsi--
# print("dekripsi")
# text = ctext
# cipher = enkripRC4(key,text)
# hex = cipherhex(cipher)
# ctext = ciphertext(cipher)
# c64 = cipher64(hex)
# print("Cipher : ",cipher)
# print("Cipher hex :",hex)
# print("Cipher str : ",ctext)
# print("Cipher Base 64 : ",c64)




  