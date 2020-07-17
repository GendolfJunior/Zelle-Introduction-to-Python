# 11. Write a program to find the first n natural numbers, where the value of n is provided by the user.

# prompt user to input value of n
# a natural number start is a = 1
# a formula to calculate sum is sum += 1
# how many times to calculate the formula is in range of n
# print out the result

# the option using arithmetic progression
def main():
    n = int(input("Enter the value of n: "))
    a1 = 1
    sum = ((2 * a1 + (n - 1)) / 2) * n
    print("The sum currently is: ", sum)


main()


# the option using controlled loop
def main2():
    n = int(input("Enter the value of n: "))
    sum = 0
    for i in range(n + 1):
        sum += i

    print("The sum currently is: ", sum)


main2()
