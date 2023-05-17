# quadratic3.py

import math


def main():
    print("This program finds the real solutions to a quadratic\ n")
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    discrim = b * b - 4 * a * c
    if discrim < 0:
        print("\ nT he eq ua tion ha s no real root s!")
    else:
        discRoot = math.sqrt(b * b - 4 * a * c)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        print("\ nT he sol utions a re :", root1, root2)
    main()
