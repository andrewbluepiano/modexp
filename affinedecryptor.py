#Author: Andrew Afonso
#An affine key decryptor. Accepts decryption key with values k=(a, b)
import string
decrypted = []
encrypted = str(input("Enter encrypted text:")).lower()
a = int(input("Enter a (key):"))
b = int(input("Enter b (key):"))
count = 0
track = 0
while track == 0:
    if ((a*count) % 26) == 1:
        print("Found it:" + str(count))
        track = 1
    else:
        count+=1
for y in encrypted:
    place = int(string.ascii_lowercase.index(y))
    print(int(place))
    plain = (count*(int(place)-b))%26
    decrypted.append(plain)
print("OUT:" + str(decrypted))
out = ""
for c in decrypted:
    new = chr(c+97)
    out += new
print(out)
