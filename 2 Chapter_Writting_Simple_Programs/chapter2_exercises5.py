# convert.py
#   A program to convert Celsius temps to Fahrenheit
# by Andriy
def main():
    print("table of Celsius and Fahrenheit tenpratures")
    celsius = 0
    for i in range(10):
        fahrenheit = 9.0/5.0 * celsius + 32
        print(str(celsius), "|" , str(fahrenheit))
        celsius += 10
main()