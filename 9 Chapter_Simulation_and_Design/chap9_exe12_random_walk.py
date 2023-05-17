# 12. A random walk is a particular kind of probabilistic simulation that models
# certain statistical systems such as the Brownian motion of molecules. You
# can think of a one-dimensional random walk in terms of coin flipping.
# Suppose you are standing on a very long straight sidewalk that extends
# both in front of and behind you. You flip a coin. If it comes up heads, you
# take a step forward; tails means to take a step backward.
# Suppose you take a random walk of n steps. On average, how many
# steps away from the starting point will you end up? Write a program to
# help you investigate this question.

# design
# print intro to the program
# get user input how many steps to simulate and assign it to the variable
# create a loop with a cycle = user inputted value
# create an int variable to record each step with a default value 0
#       toss a coin to know should you step forward or backward with randrange(0,2)
#       0 will mean -1 step
#       1 will mean +1 step
# print the result how many steps the user should make

from random import *

def simulate():
    return randrange(0, 2)


def main():
    print("A random walk calculates a probablity of stepping forward or backward")
    walk = int(input("How many steps to simulate? "))
    steps = 0
    for i in range(1, walk + 1):
        move = simulate()
        print(move)
        if move == 0:
            steps -= 1
        else:
            steps += 1

    print("user can walk ", steps)


if __name__ == '__main__':
    main()
