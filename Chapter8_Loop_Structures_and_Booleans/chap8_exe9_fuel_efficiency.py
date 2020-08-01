# 9. Write a program that computes the fuel efficiency of a multi-leg journey.
# The program will first prompt for the starting odometer reading and then
# get information about a series of legs. For each leg, the user enters the
# current odometer reading and the amount of gas used (separated by a
# space). The user signals the end of the trip with a blank line. The program
# should print out the miles per gallon achieved on each leg and the total
# MPG for the trip.

# prompt user to enter gas and miles, separated with comma
# enter a while loop which checks if the input value is not blank
#   split user entered value with a split function and comma as a separator
#   assign splitted values
#   calc current leg usage with a formula mileage/gas
#   add current milage to total mileage
#   add current gas to total fuel spending
#   prompt user to enter a new miles and gas values
#

def main():
    print("This program calculates fuel efficiency over a multi-leg journey.")
    print("You should enter the gallons of gas consumed and miles traveled")
    print("for each leg. Just hit <Enter> to signal the end of the trip.")
    print()

    distance, fuel = 0.0, 0.0
    inStr = input("Enter gallons and miles (with a comma between): ")
    while inStr != "":
        inputs = inStr.split(",")
        gallons, miles = int(inputs[0]), int(inputs[1])
        print("MPG for this leg: {0:0.1f}".format(miles / gallons))
        distance = distance + miles
        fuel = fuel + gallons
        inStr = input("Enter gallons and miles (with a comma between): ")

    print()
    print("You traveled a total of {0:0.1f} miles on {1:0.1f} gallons."
          .format(distance, fuel))
    print("The fuel efficiency was {0:0.1f} miles per gallon."
          .format(distance / fuel))


if __name__ == '__main__':
    main()
