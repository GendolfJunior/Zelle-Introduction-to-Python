# 10. Modify the previous program to get its input from a file.

def main():
    print("This program calculates fuel efficiency over a multi-leg journey.")
    print("You should enter the file with a data about gallons of gas consumed and miles traveled")
    print()

    distance, fuel = 0.0, 0.0
    fname = input("Enter filename: ")
    infile = open(fname, 'r')
    for inStr in infile.readlines():
        inputs = inStr.split(",")
        gallons, miles = float(inputs[0]), float(inputs[1])
        print("MPG for this leg: {0:0.1f}".format(miles / gallons))
        distance = distance + miles
        fuel = fuel + gallons
    infile.close()
    print()
    print("You traveled a total of {0:0.1f} miles on {1:0.1f} gallons."
          .format(distance, fuel))
    print("The fuel efficiency was {0:0.1f} miles per gallon."
          .format(distance / fuel))


if __name__ == '__main__':
    main()
