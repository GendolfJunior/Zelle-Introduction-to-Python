# input fahrenheit
# calculate equivalent in celsius
# print output results

def main():
    fahrenheit = eval(input("Enter the temprature in fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print("the temprature in celsius is: ", celsius)

main()