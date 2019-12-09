# Author: Andrew Afonso
# Finds probability of no collisions for hash function using function e^-(sum(1 -> t-1) / 365)
import sys
import math

def prob(t):
    # Probability as float
    p = math.e ** -(math.fsum(range(1, t)) / 365)
    return p

def main():
    # For single t
    if len(sys.argv) == 2:
        #Number of people
        t = int(sys.argv[1])
        print("Probability of no Collision: " + str(prob(t)))
    # For range of t
    elif len(sys.argv) == 3:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        for t in range(a, b+1):
            print("Probability of no Collision for " + str(t) + " people: " + str(prob(t)))
    else:
        print("Need a number, or range")
        exit()

if __name__ == "__main__":
    main()
