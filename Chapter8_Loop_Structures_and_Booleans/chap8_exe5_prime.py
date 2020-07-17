# 5. A positive whole number n > 2 is prime if no number between 2 and sqrt(n)
# (inclusive) evenly divides n. Write a program that accepts a value of n as
# input and determines if the value is prime. If n is not prime, your program
# should quit as soon as it finds a value that evenly divides n.

# Note. I didn't solve this problem and decided to move on to save time for learning other things.

import math


def isPrime(n):
    if n % 2 == 0:
        return False
    factor = 3
    while factor <= math.sqrt(n):
        if n % factor == 0:
            return False
        factor = factor + 2
    return True


def main():
    print("Prime number tester\n")
    n = int(input("Enter a value to test: "))
    if isPrime(n):
        print(n, "is prime.")
    else:
        print(n, "is not prime.")


if __name__ == '__main__':
    main()
