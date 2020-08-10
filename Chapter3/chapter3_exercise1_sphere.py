# 1. Write a program to calculate the volume and surface area of a sphere from
# its radius, given as input. Here are some formulas that might be useful:
# V = 4/3 * p * r^3
# A = 4 * pi * r^2

# import math library
# prompt input of radius value
# calculate volume based on formula
# cal surface area based on formula
# print out the result of volume
# print out the result of area

import math

def main():
    r = int(input("Enter a value of radius: "))
    v = 4.0 / 3.0 * math.pi * r ** 3
    a = 4 * math.pi * r ** 2
    print("the Volume is: ", v)
    print("The surface area is: ", a)


main()

