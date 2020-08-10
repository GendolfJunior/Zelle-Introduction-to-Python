# 5. Redo the programming exercise 2 from chapter 3. Use 2 functions - one to compute the area of a pizza and one to
# compute the price.

import math


def pizzaArea(radius):
    area = math.pi * radius ** 2
    return area


def cost(price, radius):
    cost = price / pizzaArea(radius)
    return cost


def main():
    r = float(input("Enter a value of radius in inches: "))
    price = float(input("Enter a price value per inch: "))
    print("the cost is: ", cost(price, r))


main()

