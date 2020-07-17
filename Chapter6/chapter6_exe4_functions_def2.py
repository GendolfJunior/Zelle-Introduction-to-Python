#  4. Write definitions for these functions:

def sumN(n):
    natural = 0
    for i in range(n + 1):
        natural = natural + i
    return natural

def sumNCubes(n):
    sumCube = 0
    for i in range(n + 1):
        cube = i ** 3
        sumCube += cube
    return sumCube

def main():
    n = int(input("Enter a sequence of natural numbers: "))
    print("the sum of", n, "natural numbers is: ", sumN(n))
    print("the sum of the cubes of", n, "natural numbers is: ", sumNCubes(n))


main()
