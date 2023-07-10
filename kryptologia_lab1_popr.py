from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

data = b'123456789'
key = get_random_bytes(32)
iv = get_random_bytes(16)
IVlist = list(iv)

cipher1 = AES.new(key, AES.MODE_CBC, iv)

ct = cipher1.encrypt(pad(data, 16))

CT=list(ct)

padingbajt=1
I = [0] * 16
DPT = [0] * 16

for y in range(15, -1, -1):

    for x in range(255):
        Cprim = list(iv)

        Cprim[y] = x

        iv = bytes(Cprim)

        if(not(x== IVlist[y] and y==15)):
            try:

                cipher2 = AES.new(key, AES.MODE_CBC, iv)

                pt = unpad(cipher2.decrypt(ct), 16)
                print('iv',iv)
                print("plaintext", pt.hex(" "))
                print("x", x)
                print('iv[15]', IVlist[y])
                print(padingbajt,'paddingbajt')

                I[y]= padingbajt ^ x
                print(I[y])
                DPT[y] = I[y] ^ IVlist[y]
                print(y)
                print('odszyfrowane : ',DPT)
                padingbajt += 1
                for z in range(padingbajt-1):

                    index = 15-z
                    #print(index)
                    Cprim = list(iv)
                    Cprim[index] = padingbajt^I[index]
                    iv = bytes(Cprim)
                break
            except ValueError: pass

liczby=list(data)
print ("odszyfrowane : ", DPT)
print("plaintext : ", liczby)

