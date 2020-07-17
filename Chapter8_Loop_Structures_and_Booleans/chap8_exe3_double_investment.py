# 3. Write a program that uses a while loop to determine how long it takes
# for an investment to double at a given interest rate. The input will be an
# annualized interest rate, and the output is the number of years it takes an
# investment to double. Note: The amount of the initial investment does not
# matter; you can use $1.

def main():
    apr = float(input("Enter the annualized interest rate: "))
    orig_principal = float(input("Enter the initial principal: "))
    calc_principal = orig_principal
    years = 0
    while calc_principal <= (orig_principal * 2):
        calc_principal = calc_principal * (1 + apr)
        years += 1
    print("It takes {0} years to double the investment. The amount will be {1}".format(years, calc_principal))


main()
