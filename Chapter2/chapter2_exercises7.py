# futval.py

# input a starting investment
# input what is fixed amount every year
# input interest rate
# input the number of years to invest
# calculate a first year investment
# calculate addition to the investment

def main():
    print("This program calculates the future value")
    years = eval(input("Enter how many years to calculate an investment as integer? "))
    principal = 0.0
    annual_additional_investment = eval(input("What is the annual additional investment? "))
    apr = eval(input("Enter the annual interest rate as decimal, e.g. 0.01: "))

    for i in range(years):
        principal += annual_additional_investment
        principal = principal * (1 + apr)
    print("The yield value in ", years," years is: ", principal)

main()
