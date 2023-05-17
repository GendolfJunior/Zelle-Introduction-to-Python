# 2. The National Weather Service computes the windchill index using the following formula:
#                   35.74 + 0.6215T - 35.75(V ** 0.16) + 0.4275T(V ** 0.16)
# Where T is the temperature in degrees Fahrenheit, and V is the wind speed in miles per hour.
# Write a program that prints a nicely formatted table of windchill values.
# Rows should represent wind speed for 0 to 50 in 5-mph increments,
# and the columns represent temperatures from -20 to + 60 in 10-degree increments.
# Note: The formula only applies for wind speeds in excess of 3 miles per hour.

#   Windchill Table

def windChill(t, v):
    if v > 3:
        chill = 35.74 + 0.6215 * t - 35.75 * (v ** 0.16) + 0.4275 * t * (v ** 0.16)
    else:
        chill = t
    return chill


def main():
    # Print table headings
    print("Wind Chill Table\n\n")
    print("Temperature".center(70))
    print("MPH|", end=' ')
    temps = list(range(-20, 61, 10))
    for t in temps:
        print("{0:5}".format(t), end=' ')
    print("\n---+" + 55 * '-')

    # Print lines in table
    for vel in range(0, 51, 5):
        print("{0:3}|".format(vel), end=' ')
        for temp in temps:
            print("{0:5.0f}".format(windChill(temp, vel)), end=' ')
        print()
    print()


main()
