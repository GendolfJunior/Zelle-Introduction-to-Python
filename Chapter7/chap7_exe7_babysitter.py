# 7. Babysitter pay
# A babysitter charges $2.50 an hour until 9:00 PM when the rate drops to
# $1.75 an hour (the children are in bed). Write a program that accepts a
# starting time and ending time in hours and minutes and calculates the total
# babysitting bill. You may assume that the starting and ending times are in
# a single 24-hour period. Partial hours should be appropriately prorated.

# Input: start and end time
# Output: calculated total amount

# algorithm
# split strings with start and end time
# convert minutes into hours and add to the hours
# calculate rate during normal hours
# calculate rate during late hours (if it is after 9 pm)
# validate inputed hours and minutes

def convertTime(time):
    # this function takes as an input time in the format e.g. 15:53 and returns a float
    startHour = time.split(':')[0:1]
    startHour = float(startHour[0])
    startMin = time.split(':')[1:2]
    startMin = (float(startMin[0])) / 60
    # if startMin > 1:
    timeConverted = startHour + startMin
    return timeConverted


def paymentCalc(start, end):
    # this function calculates payments based on time worked
    total = 0.0
    if end > 21:
        nightWork = (end - 21) * 1.75
        dayWork = (21 - start) * 2.5
        total = dayWork + nightWork
    else:
        total = (end - start) * 2.5

    return total


def main():
    startTime = input("Enter the start time (hours and minutes using ':' as a separator): ")
    endTime = input("Enter the end time (hours and minutes ':' as a separator): ")
    start = convertTime(startTime)
    end = convertTime(endTime)
    if start > end:
        print("Please verify the input parameters: ")
    else:
        total = paymentCalc(start, end)
        print(total)


if __name__ == '__main__':
    main()
