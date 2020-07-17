# c) Sum of a series of numbers entered by the user until the value 999 is entered. Note: 999 should not be part of the sum.

def main():
    sum = 0
    i = 0
    # i = input("Enter the amount (enter 999)")
    while i < 999:
        sum = sum + i
        i = int(input("Enter the amount (enter 999): "))
    print(sum)


main()
