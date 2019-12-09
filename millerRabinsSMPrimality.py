# Author: Andrew Afonso
# Primality tester: Uses Miller Rabins and Square Multiply to check if a number is a prime liar. 
from concurrent import futures
import random
import csv
import time

class testNum:
    def __init__(self, p):
        self.p = p
        self.threadpool = futures.ThreadPoolExecutor(max_workers=20)
        self.prime = 0
        self.comp = 0
        self.liar = 0
        self.done = 0
        
    def phaseone(self):
        for num in range(2, self.p - 2):
            job = self.threadpool.submit(self.mr, num)
        self.threadpool.shutdown(wait=True)
        self.done = 1
            
    def mr(self, num):
        tick = 0
        r = self.p - 1
        u = 0
        while r%2==0:
            #If a third parameter is present, it returns x to the power of y, modulus z. pow(x, y, z)
            r>>=1
            u+=1
        z = pow(num, r, self.p)
        if  z == 1 or z == (self.p - 1):
            self.comp+=1
            tick = 1
            if self.prime > 0:
                self.liar=1
        for j in range(1, u): #u-1
            if pow(num, 2**j * r, self.p) == self.p - 1:
                self.comp += 1
                tick = 1
        if tick == 0:
            self.prime += 1
        
def main():
    for odd in range(105001, 120000, 2):
        print(odd)
        testing = testNum(odd)
        testing.phaseone()
        while testing.done != 1:
            pass
        if testing.liar == 1:
            with open('output.csv', 'a', newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow([testing.p, testing.prime, testing.comp])

if __name__ == "__main__":
    main()
