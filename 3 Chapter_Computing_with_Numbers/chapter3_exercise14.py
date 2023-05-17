# 14. Write a program that finds the average of a series of numbers entered by the user. As in the previous problem, the program will first ask the
#     user how many numbers there are. Note: The average should always be a float, even if the user inputs are all ints.

def main():
    n = int(input("Input how many numbers: "))
    average = 0.0
    suma = 0.0
    for i in range(1, n + 1):
        a = float(input("Enter the number: "))
        suma += a
        average = suma / n

    print("The total sum is: " + str(suma))
    print("The average is: " + str(average))


main()
