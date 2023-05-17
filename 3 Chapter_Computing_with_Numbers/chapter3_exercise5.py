#  5. The Konidtorei coffee shop sells coffee at $10.50 a pound plus the cost of shipping. Each order ships for $.086 per pound + $1.50 fixed cost
#     for overhead. Write a program that calculates the cost of an order.

def main():
    pounds = float(input("enter how many pounds: "))
    cost = pounds * (10.50 + .86) + 1.5
    print("the cost of order is: ", cost)


main()
