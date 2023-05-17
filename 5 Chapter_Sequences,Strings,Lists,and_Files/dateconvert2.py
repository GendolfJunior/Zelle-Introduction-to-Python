# Converts a date in form "mm/dd/yyyy" to "month day, year"
# As discussed in the chapter, string formatting could be used to simplify the
# dateconvert2.py program. Go back and redo this program making use
# of the string-formatting method.

def main():
    # get the date
    dateStr = input("Enter a data (mm/dd/yyyy): ")

    # split into components
    monthStr, dayStr, yearStr = dateStr.split("/")

    # convert monthStr to the month name
    months = ["January", "February", "March", "April",
              "May", "June", "July", "August",
              "September", "October", "November", "December"]

    # output result in month day, year format
    print("The converted date is: {0} {1}, {2}".format(months[int(monthStr) - 1], dayStr, yearStr))


main()
