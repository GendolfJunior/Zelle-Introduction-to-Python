# 8. The greatest common divisor (GCD) of two values can be computed using
# Euclid's algorithm. Starting with the values m and n, we repeatedly apply
# the formula: n, m = m , n % m until m is 0. At that point, n is the GCD of
# the original m and n. Write a program that finds the GCD of two numbers using this algorithm.

def main():
    n = int(input("Enter the number N: "))
    m = int(input("Enter the number M: "))
    while m != 0:
        n, m = m, n % m
        print(n, m)
    print("final values are: ", n, m)


if __name__ == '__main__':
    main()
