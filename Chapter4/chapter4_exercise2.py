#  2. An archery target consists of a central circle of yellow surrounded by concentric rings of red, bue, black and white. Each
# #     ring has the same width, which is the same as the radius of the yellow circle. Write a program that draws such a target.
# #     Hint: Objects drawn later will appear on top of objects drawn earlier.
#
# #     Note: Add text here about algorithm design
#
# #     target.py
# #     A program to draw a target of any size and any number of rings of different color.

# create canvas window 200 x 200
# create a yellow circle in the center with a radius of 2
# create a variable for width which is the same for all rings
# create a red ring
# create a blue ring
# create a black ring
# create a white ring

from graphics import *

def main():
    win = GraphWin("Archery Target", 400, 400)
    win.setBackground("grey")
    center = Point(200, 200)
    width = 10
    circleY = Circle(center, width)
    circleY.setFill("yellow")
    circleR = Circle(center, width * 2)
    circleR.setFill("red")
    circleBlue = Circle(center, width * 3)
    circleBlue.setFill("blue")
    circleBlack = Circle(center, width * 4)
    circleBlack.setFill("black")
    circleW = Circle(center, width * 5)
    circleW.setFill("white")
    circleW.draw(win)
    circleBlack.draw(win)
    circleBlue.draw(win)
    circleR.draw(win)
    circleY.draw(win)

    # Wait for another click to exit
    win.getMouse()
    win.close()


main()