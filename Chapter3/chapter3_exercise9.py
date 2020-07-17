#  9. Write a program to calcualte the area of a triangle given the length of its three sides--a, b, and c--using these formulas:
#                                         s = (a + b + c) / 2
#                                         A = sqrt(s(s - a)(s - b)(s - c))
#
import math


def main():
    a, b, c = eval(input("Enter three sides of triangle a, b, c: "))
    s = (a + b + c) / 2  # half perimeter
    A = math.sqrt(s * (s - a) * (s - b) * (s - c))  # area of a triangle (площа)
    print("The area is: ", A)


main()
