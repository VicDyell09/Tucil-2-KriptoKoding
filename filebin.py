import pathlib

# fungsi read file in bytes
def readfilebin(filename):
    bytes=[]
    with open(filename, "rb") as f:
        while True:
            b = f.read(1)
            if not b:
                break
            bytes.append(int.from_bytes(b, byteorder="big"))
    text =""
    for i in range(len(bytes)):
        text+=chr(bytes[i])
    return(text)

#funsi write bytes ke file dengan suffix yang sama
def writefilebintofile(filename,text):
    with open("HasilExtended"+(pathlib.Path(filename).suffix),"wb") as f:
        for char in text:
            f.write(ord(char).to_bytes(1,byteorder="big"))
            

#funsi write bytes ke file txt
def writefilebin(text):
    with open("hasil.txt","ab") as f:
        for char in text:
            f.write(ord(char).to_bytes(1,byteorder="big"))
        f.write(b'\n')

# #----main-----
# filename = "abc.mkv"
# file = readfilebin(filename)
# print(file)
# writefilebin(filename,file)

