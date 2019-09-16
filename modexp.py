#Solves for x for equations in the format:
print("a^x = b mod c")
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
count = 0
track = 0
while track == 0:
	if ((a**count) % c) == b:
		print("Found it:" + str(count))
		track = 1
	else:
		count+=1
