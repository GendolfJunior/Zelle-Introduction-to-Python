# 7. The Goldbach conjecture asserts that every even number is the sum of two
# prime numbers. Write a program that gets a number from the user, checks
# to make sure that it is even, and then finds two prime numbers that add up to the number.

# Note. I didn't solve this problem and decided to move on to save time for learning other things.

import chap8_exe5_prime


def main():
    print("This program finds all prime numbers that add up to the number\n")
    n = int(input("Enter the upper limit, n: "))
    if (n % 2 == 0):
        primes = []
        for i in range(2, n + 1):
            if chap8_exe5_prime.isPrime(i):
                # print(i, end=' ')
                primes.append(i)
        print(primes)
    else:
        print("this is not an even number")


main()
