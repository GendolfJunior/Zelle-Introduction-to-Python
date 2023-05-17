# futval.py

def main():
    print("This program calculates the future value")
    years = eval(input("Enter how many years to calculate an investment as integer? "))
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate as decimal, e.g. 0.01: "))

    for i in range(years):
        principal = principal * (1 + apr)
    print("The yield value in ", years," years is: ", principal)

main()
