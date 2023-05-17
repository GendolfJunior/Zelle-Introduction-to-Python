# month.py
# A program to print the abbreviation of a month, given its number
def main():
    # month is used as a lookup table
    month = "JanFebMarAprMayJunJulAugSepOctNovDec"

    n = int(input("Enter a month number (1-12): "))

    # compute starting position of month n in month
    pos = (n - 1) * 3

    # grab the appropriate slice from months
    monthAbbrev = month[pos: pos + 3]

    # print the result
    print("The month abbreviation is: ", monthAbbrev + ".")


main()
