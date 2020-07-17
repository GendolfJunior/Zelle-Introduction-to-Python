# 13. Write a program to sum a series of numbers entered by the user. The program should first prompt the user for how many numbers are to be summed.
#     The program should then prompt the user for each of the numbers in turn and print out a total sum after all the numbers have been entered.
#     Hint: Use an input statement in the body of the loop.

# prompt a user to input how many numbers the user is willing to enter
# enter a loop based on range inputed by the user
#   in the loop prompt the user to input the number
#   in the loop sum each entered valued to the previous
# print out the result

def main():
    n = int(input("Input how many numbers: "))
    suma = 0
    for i in range(1, n + 1):
        a = int(input("Enter the number: "))
        suma += a

    print("The total sum is: " + str(suma))


main()
