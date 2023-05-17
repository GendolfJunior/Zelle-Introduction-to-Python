# 10. The formula for Easter in the previous problem works for every year in
# the range 1900-2099 except for 1954, 1981, 2049, and 2076. For these
# 4 years it produces a date that is one week too late. Modify the above
# program to work for the entire range 1900-2099.

def main():
    year = int(input("Enter the year to forecast the date of the Easter: "))
    if year in range(1900, 2099):
        a = year % 19
        b = year % 4
        c = year % 7
        d = (19 * a + 24) % 30
        e = (2 * b + 4 * c + 6 * d + 5) % 7
        easter = 22 + d + e
        exceptions = [1954, 1981, 2049, 2076]
        if year in exceptions:
            easter -= 7
        if easter > 31:
            print("Easter is on April", easter - 31)
        else:
            print("Easter is on March", easter)
    else:
        print("That's not a year between 1982 and 2048.")

if __name__ == '__main__':
    main()
