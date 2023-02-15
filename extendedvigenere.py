import numpy as np

def templatematriksext():
    matriks = np.zeros((256,256))
    for i in range (256):
        for j in range (256):
            matriks[j][i] = (i+j)%256
    return matriks

def extvigenereencrypt(kalimat, key):
    matriks = templatematriksext()
    arrkalimat = []
    arrkey = []
    for i in range (len(kalimat)):
        arrkalimat.append(kalimat[i])
    for i in range (len(key)):
        arrkey.append(key[i])

    if (len(arrkey)<len(arrkalimat)):
        for i in range(len(arrkey)+1, len(arrkalimat)+1):
            arrkey.append(arrkey[i-len(key)-1])
    else:
        arrkey = arrkey[:len(arrkalimat)]

    hasil = []

    for i in range (len(kalimat)):
        indeks1 = ord(arrkalimat[i])
        indeks2 = ord(arrkey[i])
        hasil.append(chr(int(matriks[indeks1][indeks2])))

    strhasil = ''.join(str(x) for x in hasil)

    return strhasil

def extvigeneredecrypt(kalimat, key):
    matriks = templatematriksext()
    arrkalimat = []
    arrkey = []
    for i in range (len(kalimat)):
        arrkalimat.append(kalimat[i])
    for i in range (len(key)):
        arrkey.append(key[i])

    if (len(arrkey)<len(arrkalimat)):
        for i in range(len(arrkey)+1, len(arrkalimat)+1):
            arrkey.append(arrkey[i-len(key)-1])
    else:
        arrkey = arrkey[:len(arrkalimat)]

    hasil = []

    for i in range (len(kalimat)):
        indeks2 = ord(arrkey[i])
        for j in range (256):
            if (ord(arrkalimat[i])==int(matriks[j][indeks2])):
                indeks1 = j
                hasil.append(chr(int(matriks[indeks1][0])))

    strhasil = ''.join(str(x) for x in hasil)

    return strhasil      

# tes1 = extvigenereencrypt("testkalimat","abc")
# tes2 = extvigeneredecrypt(tes1, "abc")
# print(tes1)
# print(tes2)