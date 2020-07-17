# 8. Solve Programming Exercise 17 from Chapter 3 using a function
# nextGuess (guess, x) that returns the next guess.

import math

def nextGuess(guess, x):
    guess = (guess + x / guess) / 2.0
    return guess

def main():
    x = eval(input("Enter the value X to find a square root: "))
    n = eval(input("Enter how many times to loop to find a more precise answer: "))
    guess = x / 2.0

    for i in range(n):
#        print(i)
#       print("Current guess value is: ", guess)
#        print("The sum guess + x is: ", guess + x)
#        print("x / guess = ", x / guess)
        guess = nextGuess(guess, x)

    actual = math.sqrt(x)
    print("The actual sqrt is: ", actual)
    print("The difference is: ", actual - guess)


main()
