# 11. Heating and cooling degree days are measures used by utility companies to estimate energy requirements. If the average temperature for a day is
# below 60, then the number of degrees below 60 is added to the heating degree days. If the temperature is above 80, the amount over 80 is added
# to the cooling degree days. Write a program that accepts a sequence of average daily temperatures and computes the running total of cooling and
# heating degree days. The program should print these two totals after all the data has been processed.

# tech design
# print the intro to the program
# get user input of daily averages, split by comma
# create a list to hold daily averages, use split function with comma separator to get the value for the list
# create a loop through the list
# compare each value in the list in the if with a threshhold
# create vars for heating and cooling days
# add +1 either to heating or cooling days depending on if outcome
# print both vars

def userInput():
    dataInput = input("Enter the daily temprature using a comma as a separator: ").split(",")
    return dataInput


def measures(tempratures):
    heating, cooling = 0, 0
    for i in tempratures:
        i = int(i)
        if i < 60:
            heating += 1
        elif i > 80:
            cooling += 1
        else:
            pass
    return heating, cooling


def main():
    print("this program calculates heating and cooling days!")
    tempratures = userInput()
    heating, cooling = measures(tempratures)
    print("There are {0} heating and {1} cooling days".format(heating, cooling))


if __name__ == '__main__':
    main()
