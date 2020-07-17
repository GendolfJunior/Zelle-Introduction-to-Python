# 15. Write a program tha approximates the value of pi by summing the terms of this series:
#     4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ...
#     The program should prompt the user for n, the number of terms to sum, and then output the sum of the first n terms of this series. Have your
#     program subtrac the approximation from the value of math.pi to see how accurate it is.

# prompt the user to input the number of terms to sum
# loop over the inputed n
# a = 4
# b = 2
# formula:
#         a/1 - a/3 +
#         a/(3+2) - a/(3+2+2) +
#         a/(3+2+2+2) - a/(3+2+2+2+2) ...

#     a/1 - a/3 +
#     a/(3+b) - a/(3+2b) +
#     a/(3+3b) - a/(3+4b) + ...
# print out the result

def main():
    n = int(input("Enter the number of terms to sum: "))
    a = 4
    b = 2
    sum = a - a / 3
    print("the starting sum is: ", sum)

    for i in range(1, n):
        sum += a / (3 + b * i) - a / (3 + b * (i + 1))
        print("the current sum is: ", sum)


main()

# I didn't manage to solve it ((((((((((((((((