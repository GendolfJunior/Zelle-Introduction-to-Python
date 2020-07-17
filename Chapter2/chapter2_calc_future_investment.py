def main():
    print("This program calculates the future value")
    print("of a 10-year investment")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate as decimal, e.g. 0.01: "))

    for i in range(10):
        principal = principal * (1 + apr)
    print("The yield value in 1p years is: ", principal)

main()
