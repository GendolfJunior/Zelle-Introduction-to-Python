# 12. Write a program to find the sum of the cubes of the first n natural numbers where the value of n is provided by the user.
# prompt user to input value of n
# a natural number start is a = 1
# a formula to calculate cube is a ** 3
# a formula to calculate sum is sum += a
# how many times to calculate the formula is in range of n
# print out the result

# the option using arithmetic progression

# the option using controlled loop
def main2():
    n = int(input("Enter the value of n: "))
    sum = 0
    for i in range(1, n + 1):
        a = i ** 3
        sum += a

    print("The sum of cubes currently is: ", sum)

main2()
