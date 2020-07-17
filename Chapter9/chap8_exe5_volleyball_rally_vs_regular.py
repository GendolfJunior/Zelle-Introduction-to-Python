# 5. Design and implement a system that compares regular volleyball games
# to those using rally scoring. Your program should be able to investigate
# whether rally scoring magnifies, reduces, or has no effect on the relative
# advantage enjoyed by the better team.

from random import *


def main():
    printlntro()
    probA, probB, n = getlnputs()
    winsA, winsB, winsA_rally, winsB_rally = simNGames(n, probA, probB)
    printSummary(winsA, winsB, winsA_rally, winsB_rally)


def printlntro():
    print("This program simulates a game of volleyball between two")
    print('Teams called "A" and "B". The ability of each team is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the team wins the point when serving. team A always")
    print("has the first serve.")


def getlnputs():
    # Returns the three simulation parameters
    a = float(input("What is the prob. team A wins a serve? "))
    b = float(input("What is the prob. team B wins a serve? "))
    n = int(input("How many games to simulate? "))
    return a, b, n


def simNGames(n, probA, probB):
    # Simulates n games of volleyball between teams whose
    # abilities are represented by the probability of winning a serve.
    # Returns number of wins for A and B
    winsA = winsB = 0
    winsA_rally = winsB_rally = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    for i in range(n):
        scoreA_rally, scoreB_rally = simOneGame_rally(probA, probB)
        if scoreA_rally > scoreB_rally:
            winsA_rally = winsA_rally + 1
        else:
            winsB_rally = winsB_rally + 1

    return winsA, winsB, winsA_rally, winsB_rally


def simOneGame(probA, probB):
    # Simulates a single game or volleyball between teams whose
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


def simOneGame_rally(probA, probB):
    # Simulates a single game or volleyball between teams whose
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
                scoreB = scoreB + 1
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
                scoreA = scoreA + 1
    return scoreA, scoreB


def gameOver(a, b):
    # a and b represent scores for a volleyball game
    # Returns True if the game is over, False otherwise.
    return (a > 15 or b > 15) and ((a - b >= 2) or (b - a >= 2))


def servings():
    # this function generates a random number in the range from 1 to 10 inclusively. If the number is even serves player B,
    # otherwise serves player A
    order = randrange(1, 11)
    if (order % 2 != 0):
        serving = 'A'
    else:
        serving = 'B'
    return serving


def printSummary(winsA, winsB, winsA_rally, winsB_rally):
    # Prints a summary of wins for each team.
    n = winsA + winsB
    n2 = winsA_rally + winsB_rally
    print("\nGames simulated: ", n, n2)
    print("Wins for A: {0} ({1: 0.1%}) | ".format(winsA, winsA / n), end=' ')
    print("Wins for A rally: {0} ({1: 0.1%})".format(winsA_rally, winsA_rally / n), end=' | ')
    print("The difference is: {0} ({1: 0.1%}) ".format(winsA - winsA_rally, (winsA - winsA_rally) / n))
    print("Wins for B: {0} ({1: 0.1%}) | ".format(winsB, winsB / n), end=' ')
    print("Wins for B rally: {0} ({1: 0.1%})".format(winsB_rally, winsB_rally / n), end=' | ')
    print("The difference is: {0} ({1: 0.1%}) ".format(winsB - winsB_rally, (winsB - winsB_rally) / n))


if __name__ == '__main__':
    main()
