#  4. Write a program that determines the distance to a lightning strike based on the time elapsed between the flash and the sound of thunder.
#     The speed of sound is approximately 1100 ft/sec and 1 mile is 5280 ft.
# it is in meters 335.28/sec

# prompt a user to input time elapsed after the lighting strike
# calculate distance using formula time * 335.28
# print out the result

def main():
    time = int(input("Enter the time elapsed after the strike: "))
    distance = time * 335.28 / 1000
    print("The distance to the lightning in km is: ", distance)


main()