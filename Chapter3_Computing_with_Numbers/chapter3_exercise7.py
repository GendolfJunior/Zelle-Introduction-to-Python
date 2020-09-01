#  7. Write a program that accepts two points (see previous problem) and determins the distance between them.
#     distances = sqrt((x2-x1)^2 + (y2-y1)^2)
import math

def main():
    x1, y1 = eval(input("enter x1 and y1, using comma ',' as a separator : "))
    x2, y2 = eval(input("enter x2 and y2, using comma ',' as a separator : "))
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print(distance)


main()
