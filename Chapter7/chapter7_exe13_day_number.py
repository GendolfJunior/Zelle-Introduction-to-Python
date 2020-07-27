# 13. The days of the year are often numbered from 1 through 365 (or 366).
# This number can be computed in three steps using int arithmetic:
#       (a) dayNum = 31(month - 1) + day
#       (b) if the month is after February subtract (4 (month) + 23) // 10
#       (c) if it's a leap year and after February 29, add 1
# Write a program that accepts a date as month/day/year, verifies that it is a
# valid date (see previous problem), and then calculates the corresponding day number.

# design
# get input date in the format month/day/year
# subtract each part of the date
# validate date and if it is not correct terminate the program and output what is wrong with the date
# calc formula a)
# if condition is true calc formula b) for month February
# if this is a leap year then in calc of the day + 1

# c07ex12.py
#    Date validator
from Chapter7.c07ex11 import isLeap

DAYS_IN_MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def isValidDate(month, day, year):
    if 1 <= month <= 12:
        # month OK, check day

        # determine last day of month
        if month == 2:
            if isLeap(year):
                lastDay = 29
            else:
                lastDay = 28
        else:
            lastDay = DAYS_IN_MONTH[month]

        # if day is also good, return True
        if 1 <= day <= lastDay:
            return True

    # did not validate
    return False


def main():
    print("Date Validator\n")
    month, day, year = input("Enter a date (mm/dd/yyyy): ").split("/")
    if not isValidDate(int(month), int(day), int(year)):
        print("The date is invalid.")
    else:
        print("The date is valid.")
        month, day, year = int(month), int(day), int(year)
        print(month, day, year)
        dayNum = 31 * (month - 1) + day
        print("first dayNum", dayNum)

        if month > 2:
            print("before month>2: ", dayNum)
            dayNum = dayNum - (4 * month + 23) // 10
            print("after month>2: ", dayNum)

            if isLeap(year):
                dayNum += 1
                print('inside isLeap: ', dayNum)

        print("The date's corresponding number in the year is: ", dayNum)


if __name__ == '__main__':
    main()
