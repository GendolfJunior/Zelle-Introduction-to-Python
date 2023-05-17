# 2. The National Weather Service computes the windchill index using the following formula:
#                   35.74 + 0.6215T - 35.75(V ** 0.16) + 0.4275T(V ** 0.16)
# Where T is the temperature in degrees Fahrenheit, and V is the wind speed in miles per hour.
# Write a program that prints a nicely formatted table of windchill values.
# Rows should represent wind speed for 0 to 50 in 5-mph increments,
# and the columns represent temperatures from -20 to + 60 in 10-degree increments.
# Note: The formula only applies for wind speeds in excess of 3 miles per hour.

# Spec:
# Input 1: wind V = 0 miles/hr, increment +5, max 50
# Input 2: temprature T = -20, increment +10, max 60
# Output 1: first row wiht table columns is a temprature
# Output 2: all other rows are
# Algorithm:
# assign variables to v=5 and t=-20
# create a first row with temprature columns using an increment of +10
# print column row with formating
# create a loop to print out the values for each wind speed


def main():
    v = 5
    t = -20
    for i in range(-20, 61, 10):
        print("{0:5}".format(i), end=' ')


main()
