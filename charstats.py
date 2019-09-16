#Author: Andrew Afonso
#Description: Feed it a string, it will give you the frequency of each letter. 
encrypted = input("Enter string:")
track = []
for y in encrypted:
	if y not in track:
		print(y + " " + str(encrypted.count(y)) + " " + str( (encrypted.count(y) * 100 ) / len(encrypted) )  + "%")
		track.append(y)
