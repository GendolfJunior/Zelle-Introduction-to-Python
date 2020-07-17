# convert.py
#   A program to convert Celsius temps to Fahrenheit
# by Andriy
def main():
    for i in range(5):
        celsius = eval(input("What is the Celsius temprature? "))
        fahrenheit = 9/5 * celsius + 32
        print("The temprature is", fahrenheit, " degrees Fahrenheit")

main()