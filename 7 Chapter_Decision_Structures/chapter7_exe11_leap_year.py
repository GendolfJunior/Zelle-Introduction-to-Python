# 11. A year is a leap year if it is divisible by 4, unless it is a century year that is
# not divisible by 400. (1800 and 1900 are not leap years while 1600 and
# 2000 are.) Write a program that calculates whether a year is a leap year.

def main():
    year = int(input("Enter the year to check if it is leap year: "))
    year_leap = ''
    if (year % 4 == 0):
        year_leap = "is the leap year"
    else:
        if (year % 100 == 0):
            if (year % 400) == 0:
                year_leap = "is the leap year"
            else:
                year_leap = 'is not the leap year'
        else:
            year_leap = 'is not the leap year'
    print(year, year_leap)


if __name__ == '__main__':
    main()
