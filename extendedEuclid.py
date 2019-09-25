#Author: Andrew Afonso
import math
track = 0
aay = int(input("Enter A:"))
bee = int(input("Enter B:"))
print("")
aays = []
bees = []
ques = []
ares = []
exes = []
whys = []
exprimes = []
whyprimes = []
gcd = math.gcd(aay, bee)
print("a   b   q   r")
print("-------------")
def findPhi( thenum ):
    count = 0
    track = 0
    while count < thenum:
        outp = math.gcd(thenum, count)
        if outp == 1:
            track+=1
        count+=1
    return track;


while bee != 0:
    aays.append(aay)
    bees.append(bee)
    are = aay % bee
    ares.append(are)
    que = (aay - are) / bee
    ques.append(que)
    print(str(aay) + "  " + str(bee) + "  " + str(int(que)) + "  " + str(are))
    aay = bee
    bee = are
    track+=1

ex = 0
why = 1
exprime = 1
whyprime = 0



while track > 0:
    exes.append(ex)
    whys.append(why)
    exprimes.append(exprime)
    whyprimes.append(whyprime)
    #print(str(ex) + "  " + str(why) + "  " + str(exprime) + "  " + str(whyprime))
    ex = why #x is new
    exprime = whyprime #exprime is new
    whyprime = why #whyprime is new
    #now calculate new why
    #print(str(aays[track-1]) + "  " + str(bees[track-1]))
    track-=1
    why = (math.gcd(aays[track-1], bees[track-1]) - (ex*(aays[track-1]))) / bees[track-1]

exes.reverse()
whys.reverse()
exprimes.reverse()
whyprimes.reverse()
print("")
print("x   y   x'   y'")
print("-------------")
for x in range(0, len(whys)):
    print(str(int(exes[x])) + "  " + str(int(whys[x])) + "  " + str(int(exprimes[x])) + "  " + str(int(whyprimes[x])))
