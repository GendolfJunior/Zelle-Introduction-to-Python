# 6. Modify the previous program to find every prime number less than or equal to n.

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
    print("This program finds all prime numbers up to N\n")
    n = int(input("Enter the upper limit, n: "))
    print("primes: ", end=' ')
    for i in range(2, n+1):
        if isPrime(i):
            print(i, end=' ')
    print("Done")


if __name__ == '__main__':
    main()
