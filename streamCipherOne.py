#Author: Andrew Afonso
import string
decrypted = []
encrypted = str(input("Enter encrypted text:")).lower()
key = str(input("Enter the (key):"))
for y in range(0, len(encrypted)):
    keychar = key[y]
    encryptchar = encrypted[y]
    keyint = ord(keychar)-97
    thecharint = ord(encryptchar)-97
    newchar = (thecharint - keyint) % 26
    decrypted.append(chr(newchar + 97))
print(" ".join(decrypted))
