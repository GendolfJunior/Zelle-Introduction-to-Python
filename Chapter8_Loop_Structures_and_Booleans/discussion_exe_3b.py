# b) Sum of the first n odd numbers: 1 + 3 + 5 + . . . + 2n - 1

def main():
    n = int(input("Enter how many first odd numbers you'd like to sum: "))
    sum = 0
    i = 1
    while i < 2 * n:
        sum = sum + i
        i = i + 2
    print("the result is: ", sum)


main()
