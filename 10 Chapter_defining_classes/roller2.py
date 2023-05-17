# roller.py
# Graphics program to roll a pair of dice. uses custom widgets
# Circle Button and DieView
# this is program for Exercise 7 and 8

#  7. Write a modified Button class that creates circular buttons. Call your class
#  CButton and implement the exact same methods that are in the existing
#  Button class. Your constructor should take the center of the button
#  and its radius as normal parameters. Place your class in a module called
#  cbutton.py. Test your class by modifying roller.py to use your buttons.

# 8. Modify the Die View class from the chapter by adding a method that allows
# the color of the pips to be specified.
#       setColor(self, color) Changes the color of the pips to color.
# Hints : You can change the color by changing the value of the instance
# variable foreground, but you also need to redraw the die after doing this.
# Modify set Value so that it remembers the value of the die in an instance
# variable. Then setColor can call setValue and pass the stored value to
# redraw the die. You can test your new class with the roller.py program.
# Have the dice change to a random color after each roll (you can generate
# a random color with the color _rgb function).

from random import randrange

from graphics import GraphWin, Point

from Chapter10_defining_classes.cbutton import CButton
from Chapter10_defining_classes.dieview import DieView


def main():
    # create the application window
    win = GraphWin("Dice Roller", 400, 400)
    win.setCoords(0, 0, 10, 10)
    win.setBackground("green2")

    # Draw the interface widgets
    die1 = DieView(win, Point(3, 7), 2)
    die2 = DieView(win, Point(7, 7), 2)
    rollButton = CButton(win, Point(5, 4.5), 1, "Roll Dice")
    rollButton.activate()
    quitButton = CButton(win, Point(5, 1), 1, "Quit")

    # Event loop
    pt = win.getMouse()
    while not quitButton.clicked(pt):
        if rollButton.clicked(pt):
            value1 = randrange(1, 7)
            die1.setValue(value1)
            value2 = randrange(1, 7)
            die2.setValue(value2)
            quitButton.activate()
        pt = win.getMouse()

    # close up shop
    win.close()


main()
