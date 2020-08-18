# 13. Suppose you are doing a random walk (see previous problem) on the
# blocks of a city street. At each "step" you choose to walk one block (at
# random) either forward, backward, left or right. In n steps, how far do
# you expect to be from your starting point? Write a program to help answer this question.

from random import *

def simulate(walk):
    for i in range(1, walk + 1):
        x, y = 0, 0  # start at the origin
        dir = randrange(4)
        if dir == 0:  # go left
            x = x - 1
        elif dir == 1:  # go up
            y = y + 1
        elif dir == 2:  # go right
            x = x + 1
        else:  # go down
            y = y - 1

    return (x * x + y * y) ** .5  # distance to origin. the same expression as if to use sqrt


def main():
    print("A random walk calculates a probablity of stepping forward or backward")
    walk = int(input("How many steps to simulate? "))
    steps = simulate(walk)
    print("user can walk ", steps)


if __name__ == '__main__':
    main()
