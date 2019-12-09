# Author: Andrew Afonso
# Finds probability of no birthday collisions for t people. Outputs things to a CSV file birthday.csv
import sys
import csv

def prob(t):
    # Probability as float
    p = 0.0
    # Calculate no collision probability from 1 to t-1
    for x in range(1, t):
        if x == 1:
            p = (1 - (x / 365))
        else:
            p = p * (1 - (x / 365))
    return p

def main():
    # For single t
    if len(sys.argv) == 2:
        #Number of people
        t = int(sys.argv[1])
        print("Probability of no Birthday Collision: " + str(prob(t)))
    # For range of t
    elif len(sys.argv) == 3:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        with open('birthday.csv', 'a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            for t in range(a, b+1):
                csvwriter.writerow([str(t), str(prob(t))])
                print("Probability of no Birthday Collision for " + str(t) + " people: " + str(prob(t)))
    else:
        print("Need a number, or range")
        exit()

if __name__ == "__main__":
    main()
