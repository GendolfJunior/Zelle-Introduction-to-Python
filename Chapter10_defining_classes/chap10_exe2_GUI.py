# 2. Use the Button class discussed in this chapter to build a GUI for one (or
# more) of your projects from previous chapters.
# rball.py
from random import random

from Chapter10_defining_classes.button import *

from graphics import *

def main():
#    printlntro()
    # create animation window
    win = GraphWin("Monte Carlo simulation", 420, 420)
    win.setCoords(0, 0, 200, 200)
    win.setBackground("green2")

    intro = Text(Point(100, 100),
         "This program simulates a game of racquetball between two\nplayers called 'A' and 'B'. The ability of each player is\n"
         "indicated by a probability (a number between 0 and 1) that\nthe player wins the point when serving. Player A always\nhas the first serve.")
    intro.draw(win)
    # create a button to simulate the game or quit
    simulate = Button(win, Point(25, 20), 40, 10, "simulate")
    simulate.activate()
    quitButton = Button(win, Point(175, 20), 20, 10, "Quit")

    # Event loop
    pt = win.getMouse()
    while not quitButton.clicked(pt):
        if simulate.clicked(pt):
            intro.undraw()
            # create labels for inputs
            textA = Text(Point(60, 150), "Prob A: ")
            textA.draw(win)
            textB = Text(Point(60, 100), "Prob B: ")
            textB.draw(win)
            textN = Text(Point(60, 50), " n: ")
            textN.draw(win)
            # create Ok button
            ok = Button(win, Point(100, 10), 20, 20, "OK")
            ok.activate()
            # get input fields
            get_probA = Entry(Point(90, 150), 5)
            get_probA.setText("0.0")
            get_probA.draw(win)
            get_probB = Entry(Point(90, 100), 5)
            get_probB.setText("0.0")
            get_probB.draw(win)
            get_n = Entry(Point(90, 50), 5)
            get_n.setText("0")
            get_n.draw(win)
            # convert inputs
            probA = float(get_probA.getText())
            probB = float(get_probB.getText())
            n = int(get_n.getText())
            print(probA, probB, n)
            click = win.getMouse()

            # remove text input labels
            textA.undraw()
            textB.undraw()
            textN.undraw()

            if ok.clicked(click):
                winsA, winsB = simNGames(n, probA, probB)
                printSummary(winsA, winsB)
            quitButton.activate()
        pt = win.getMouse()

    # close up shop
    win.close()


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
    serving = "A"
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


def printSummary(winsA, winsB):
    # Prints a summary of wins for each player.
    n = winsA + winsB
    print("\nGames simulated: ", n)
    print("Wins for A: {0} ({1:0.1%})".format(winsA, winsA / n))
    print("Wins for B: {0} ({1:0.1%})".format(winsB, winsB / n))


if __name__ == '__main__':
    main()
