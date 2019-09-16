#Author: Andrew Afonso
#Description: Runs Euler’s phi function
import math
count = 0
track = 0
thenum = int(input("Enter Number:"))
while count < thenum:
	outp = math.gcd(thenum, count)
	print("GCD ("+ str(thenum) + ", " + str(count) + "): " + str(outp))
	if outp == 1:
		track+=1
	count+=1
print("Phi num: " + str(track))
