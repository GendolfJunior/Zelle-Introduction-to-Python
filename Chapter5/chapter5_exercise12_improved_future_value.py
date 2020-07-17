# Write an improved version of the futval . py program from Chapter 2. Your program will prompt the user for the amount of the investment, the
# annualized interest rate, and the number of years of the investment. The program will then output a nicely formatted table that tracks the value of
# the investment year by year. Your output might look something like this:
# Year Value
# ----------------
# 0 $2000 . 00
# 1 $2200 . 00
# 2 $2420 . 00
# 3 $2662 . 00
# 4 $2928 . 20
# 5 $322 1 . 02
# 6 $3542 . 12
# 7 $3897 . 43

def main():
    print("This program calculates the future value")
    print("of a 10-year investment")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate as decimal, e.g. 0.01: "))
    years = eval(input("Enter how many years of investment: "))

    print("Year            Value")
    print("-------------------------")

    for i in range(years + 1):
        print("{0:3} {1:18.2f}".format(i, principal))
        principal = principal * (1 + apr)


main()
