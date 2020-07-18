# 12. Write a program that accepts a date in the form month/day/year and outputs
# whether or not the date is valid. For example 5/24/1962 is valid, but
# 9/31/2000 is not. (September has only 30 days.)

def validate_month(date):
    # this is a function to validate the month
    if 0 < int(date[0]) < 13:
        return True
    else:
        return False


def day_check(month, day, month_period):
    # this function takes day and month of the date, leap year or not, and validates if the day is within the allowed range
    try:
        day_check = int(month_period[month - 1].split(":")[1])
        if (day > day_check) or (day < 1):
            return False
        else:
            return True
    except IndexError:
        print("The month is invalid!")

def leap(year):
    # this is a function to check whether the year is a leap year
    if year % 4 != 0:
        return False
    elif year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    else:
        return True


def validate_day(date):
    # this function takes date, breaks it on month, day, year parts.
    # checks if the year is leap one
    # validates the inputed day in the date
    month_reg = ["1:31", "2:28", "3:31", "4:30", "5:31", "6:30", "7:31", "8:31", "9:30", "10:31", "11:30", "12:31"]
    month_leap = ["1:31", "2:29", "3:31", "4:30", "5:31", "6:30", "7:31", "8:31", "9:30", "10:31", "11:30",
                  "12:31"]
    month = int(date[0])
    day = int(date[1])
    year = int(date[2])
    if (leap(year) == True):
        if month == 2:
            # check if this is February
            return day_check(month, day, month_leap)
        else:
            return day_check(month, day, month_reg)

    else:
        if month == 2:
            # check if this is February
            return day_check(month, day, month_reg)
        else:
            return day_check(month, day, month_reg)


def validate_year(date):
    # this function validates inputed year
    if 0 < int(date[2]) < 2099:
        return True
    else:
        return False


def main():
    input_date = input("Enter the date (MM/DD/YYYY) to be validated, using '/' as separator: ")
    date = input_date.split('/')
    if validate_year(date):
        if validate_month(date):
            if validate_day(date):
                print("The date {0} is valid".format(input_date))
            else:
                print("The date {0} is invalid".format(input_date))
        else:
            print("The month in the date {0} is invalid".format(input_date))
    else:
        print("The year in the date {0} is invalid".format(input_date))


if __name__ == '__main__':
    main()
