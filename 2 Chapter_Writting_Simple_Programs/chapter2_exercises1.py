# convert.py
#   A program to convert Celsius temps to Fahrenheit
# by Andriy
def main():
    print("This program converts inputed by a user Celsius degrees to Fahrenheit")
    celsius = eval(input("What is the Celsius temprature? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temprature is", fahrenheit, " degrees Fahrenheit")

main()