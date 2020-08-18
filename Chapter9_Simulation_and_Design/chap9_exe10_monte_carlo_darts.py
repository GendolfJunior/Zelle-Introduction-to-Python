# 10. Monte Carlo techniques can be used to estimate the value of pi. Suppose
# you have a round dartboard that just fits inside of a square cabinet. If you throw darts randomly,
# the proportion that hit the dartboard vs. those that hit the cabinet (in the corners not covered by the board) will be determined
# by the relative area of the dartboard and the cabinet. If n is the
# total number of darts randomly thrown (that land within the confines of the cabinet),
# and h is the number that hit the board, it is easy to show that
#           п ~ 4 * (h/n)
# Write a program that accepts the "number of darts" as an input and
# then performs a simulation to estimate п. Hint: You can use 2*random() - 1
# to generate the x and y coordinates of a random point inside a 2x2
# square centered at (0, 0). The point lies inside the inscribed circle if x^2 + y^2 <= 1.

# c09ex10.py
#    Monte Carlo estimation of pi
# I looked up the answer.

from random import random

def main():
    print("This program estimates the value of pi using")
    print('random "dart" tosses.')
    n = int(input("\nHow many darts should I simulate? "))
    hits = throwDarts(n)
    print("Estimated value of pi =", 4.0 * hits / n)

def throwDarts(n):
    hits = 0
    for i in range(n):
        x = 2 * random() - 1
        print("print x ", x)
        y = 2 * random() - 1
        print("print y ", y)
        if x*x + y*y <= 1:
            hits = hits + 1
            print("current hits is: ", hits)
    return hits

if __name__ == '__main__':
    main()
