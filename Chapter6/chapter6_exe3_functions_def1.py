#  3. Write definitions for these functions:
import math


def sphereArea(radius):
    a = 4 * math.pi * radius ** 2
    return a


def sphereVolume(radius):
    v = 4 / 3 * math.pi * radius ** 3
    return v


# use your functions to solve Programming Exercise 1 from chapter 3

def main():
    r = int(input("Enter a value of radius: "))
    a = sphereArea(r)
    v = sphereVolume(r)
    print("The surface area is: ", a)
    print("the Volume is: ", v)


main()
