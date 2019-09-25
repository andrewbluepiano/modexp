#Author: Andrew Afonso
#Description: For Crypto HW3 Q2, a mod n order finder
import math
ayy = 0
track = 0
enn = int(input("Enter Number:"))
print("")
primitives = []
def findPhi( thenum ):
    count = 0
    track = 0
    while count < thenum:
        outp = math.gcd(thenum, count)
        if outp == 1:
            track+=1
        count+=1
    return track;

phi = findPhi(enn)
while ayy < enn:
    outp = math.gcd(enn, ayy)
    if outp == 1:
        order = []
        ticker = 0
        eye = 0
        while ticker == 0:
            outfunc = (ayy ** eye) % enn
            if (outfunc == 1) and (eye != 0):
                order.append(outfunc)
                orderval = len(order)-1
                print("Cycle len for " + str(ayy) + " mod " + str(enn) + " = " + str(orderval) + "; ")
                print(str(ayy) + " mod " + str(enn) + ": " + str(order))
                if phi == orderval:
                    primitives.append(ayy)
                ticker=1
            else:
                order.append(outfunc)
                eye+=1
    else:
        print("GCD Failure for " + str(ayy) + "; GCD= " + str(outp))
    ayy+=1
print("Primitive roots at: " + str(primitives))

