# 9. A formula for computing Easter in the years 1982-2048, inclusive, is as
# follows: let a = year%19, b = year%4, c = year%7, d = (19a + 24)%30,
# e = (2b + 4c + 6d + 5)%7. The date of Easter is March 22 + d + e (which could be in April).
# Write a program that inputs a year, verifies that it is in
# the proper range, and then prints out the date of Easter that year.

def main():
    year = int(input("Enter the year to forecast the date of the Easter: "))
    if year in range(1982, 2048):
        a = year % 19
        b = year % 4
        c = year % 7
        d = (19 * a + 24) % 30
        e = (2 * b + 4 * c + 6 * d + 5) % 7
        easter = 22 + d + e
        if easter > 31:
            print("Easter is on April", easter - 31)
        else:
            print("Easter is on March", easter)
    else:
        print("That's not a year between 1982 and 2048.")

if __name__ == '__main__':
    main()
