# input interest rate
# input periods
# input amount
# calc periodical rate as (1 + apr) / periods

def main():
    print("This program calculates the future value as compound interest")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate as decimal, e.g. 0.01: "))
    periods = eval(input("Enter how many periods when the rate is compound: "))
    quarter_apr = (1 + apr) / periods

    for i in range(10 * periods):
        principal = principal * quarter_apr
    print("The yield value in 1p years is: ", principal)

main()
