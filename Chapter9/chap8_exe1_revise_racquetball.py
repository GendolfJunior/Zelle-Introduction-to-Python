# Revise the racquetball simulation so that it computes the results for best
# of n game matches. First service alternates, so player A serves first in the
# odd games of the match, and player B serves first in the even games.

# rball2.py

# my implementation is a bit different because I didn't understood the ask

from random import *


def main():
    printlntro()
    probA, probB, n = getlnputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)


def printlntro():
    print("This program simulates a game of racquetball between two")
    print('players called "A" and "B". The ability of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving. Player A always")
    print("has the first serve.")


def getlnputs():
    # Returns the three simulation parameters
    a = float(input("What is the prob. player A wins a serve? "))
    b = float(input("What is the prob. player B wins a serve? "))
    n = int(input("How many games to simulate? "))
    return a, b, n


def simNGames(n, probA, probB):
    # Simulates n games of racquetball between players whose
    # abilities are represented by the probability of winning a serve.
    # Returns number of wins for A and B
    winsA = winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB


def simOneGame(probA, probB):
    # Simulates a single game or racquetball between players whose
    # abilities are represented by the probability of winning a serve.
    # Returns final scores for A and B
    serving = servings()
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
    return scoreA, scoreB


def gameOver(a, b):
    # a and b represent scores for a racquetball game
    # Returns True if the game is over, False otherwise.
    return a == 15 or b == 15


def servings():
    # this function generates a random number in the range from 1 to 10 inclusively. If the number is even serves player B,
    # otherwise serves player A
    order = randrange(1, 11)
    if (order % 2 != 0):
        serving = 'A'
    else:
        serving = 'B'
    return serving


def printSummary(winsA, winsB):
    # Prints a summary of wins for each player.
    n = winsA + winsB
    print("\nGames simulated: ", n)
    print("Wins for A: {0} ({1: 0.1%})".format(winsA, winsA / n))
    print("Wins for B: {0} ({1: 0.1%})".format(winsB, winsB / n))


if __name__ == '__main__':
    main()
