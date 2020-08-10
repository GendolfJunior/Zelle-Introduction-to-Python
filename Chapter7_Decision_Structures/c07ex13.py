# c07ex13.py
#    Day number calculation

from Chapter7_Decision_Structures.c07ex11 import isLeap
from Chapter7_Decision_Structures.c07ex12 import isValidDate


def dayNumber(month, day, year):
    dayNum = 31 * (month - 1) + day
    print("first dayNum", dayNum)

    if month > 2:
        print("before month>2: ", dayNum)
        dayNum = dayNum - (4 * month + 23) // 10
        print("after month>2: ", dayNum)

    if isLeap(year):
        if month > 2:
            dayNum = dayNum + 1

    return dayNum


def main():
    print("Day number calculation\n")

    month, day, year = input("Enter date (mm/dd/yyyy): ").split("/")
    day, month, year = int(day), int(month), int(year)

    if isValidDate(month, day, year):
        print("The day number is", dayNumber(month, day, year))
    else:
        print("That's an invalid date!")


if __name__ == '__main__':
    main()
