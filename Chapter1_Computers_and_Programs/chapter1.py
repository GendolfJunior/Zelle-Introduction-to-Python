# +, -, *, /, ** (степінь), % - залишок ,  // - скільки цілих (наприклад 20//6 = 3), унарний мінус, округлення, число Пі,

# exercise 1
print("Hello, World!")
print("Hello", "World!")
print(3)
print(3.0)
print(2 + 3)
print(2.0 + 3.0)
print("2" + "3")
print("2 + 3 = ", 2 + 3)
print(2 * 3)
print(2 ** 3)
print(7 / 3)
print(7 // 3)

# exercise 3
# Modify the chaos program using 2.0 in place of 3.9 as the multiplier in the logistic function.
#Your modified line of code should look like this:
# X = 2. 0 * X * (1 - X)

def main():
    print("This program illustrates a chaotic function (Exercise 3) ")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 2.0 * x * (1 - x)
        print(x)

# main()

# exercise 4
# Modify the chaos program so that it prints out 20 values instead of 10.
def main():
    print("This program illustrates a chaotic function (Exercise 4) ")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(20):
        x = 2.0 * x * (1 - x)
        print(x)

# main()

# exercise 5
# Modify the chaos program so that the number of values to print is determined
# by the user. You will have to add a line near the top of the program
# to get another value from the user.
def main():
    print("This program illustrates a chaotic function (Exercise 5) ")
    x = eval(input("Enter a number between 0 and 1: "))
    output_times = input("Enter how many times to print out the calc results: ")

    for i in range(int(output_times)):
        x = 2.0 * x * (1 - x)
        print(x)

# main()

# exercise 6
# The calculation performed in the chaos program can be written in a number
# of ways that are algebraically equivalent. Write a version of the program
# for each of the following ways of doing the computation. Have your
# modified programs print out 100 iterations of the calculation and compare
# the results when run on the same input.
def main():
    print("This program illustrates a chaotic function (Exercise 6) ")
    x = eval(input("Enter a number between 0 and 1: "))
    output_times = input("Enter how many times to print out the calc results: ")
    y = x
    z = x

    for i in range(int(output_times)):
        x = 3.9 * x * (1 - x)
        print("The results of 'x = 3.9 * x * (1 - x)' are: ")
        print(x)
        y = 3.9 * (y - y * y)
        print("The results of 'y = 3.9 * (y - y * y)' are: ")
        print(y)
        z = 3.9 * z - 3.9 * z * z
        print("The results of 'z = 3.9 * z - 3.9 * z * z' are: ")
        print(z)
        print("--------------------------------------------------")

#main()

# exercise 7
# Modify the chaos program so that it prints out 20 values instead of 10.
def main():
    print("This program illustrates a chaotic function (Exercise 7) ")
    x = eval(input("Enter a number between 0 and 1 for the left column: "))
    a = eval(input("Enter a number between 0 and 1 for the right column: "))
    output_times = input("Enter how many times to print out the calc results: ")

    print("Input ", str(x), "         ", str(a))
    print("-----------------------------------------------")

    for i in range(int(output_times)):
        x = 3.9 * x * (1 - x)
        a = 3.9 * a * (1 - a)
        print("      ", str(x.__round__(5)), "   |  ", str(a.__round__(5)))
main()