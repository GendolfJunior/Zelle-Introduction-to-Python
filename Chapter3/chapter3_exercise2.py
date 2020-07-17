
import math

def main():
    r = float(input("Enter a value of radius in inches: "))
    price = float(input("Enter a price value per inch: "))
    area = math.pi * r ** 2
    cost = price / area
    print("the cost is: ", cost)


main()