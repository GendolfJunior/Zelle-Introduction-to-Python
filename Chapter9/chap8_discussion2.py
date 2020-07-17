# a) A random int in the range 0-10
# b) A random float in the range -0.5-0.5
# c) A random number representing the roll of a six-sided die
# d) A random number representing the sum resulting from rolling two six-sided dice
# e) A random float in the range -10.0-10.0

from random import *


def main():
    print("a: ", randrange(0, 10))
    print("b: ", uniform(-0.5, 0.5))
    print("c: ", randrange(1, 7))
    print("d: ", randrange(1, 7) + randrange(1, 6))
    print("e: ", uniform(-10, 10))
    order = randrange(1, 11)
    print(order)
    if (order % 2 != 0):
        serving = 'A'
    else:
        serving = 'B'
    print("Serves: ", serving)


main()
