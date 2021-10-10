#     target.py
#     A program to draw a target of any size and any number of rings of different color.

from graphics import *


def main():
    squareside = 200  # single point of control that allows resizing of target
    r = (squareside / 2)
    center = Point((squareside / 2), (squareside / 2))
    color = ["white", "black", "blue", "red", "yellow",
             "green"]  # use this list to add or delete colors for simpler or more complex targets

    win = GraphWin("Ready, Aim, Fire!", squareside, squareside)

    for i in range(len(color)):  # len() is used so that a target of any number of circles can be drawn

        aim = Circle(center, r - (r * (i / len(color))))  # len(0 is used to get the proportion of part to whole
        print("i is = ", i, r - (r * (i / len(color))))
        aim.setFill(color[i])
        aim.draw(win)
    # Wait for another click to exit
    win.getMouse()
    win.close()


main()

#    Another idea for a solution: Is it possible to pass a decision structure (e.g., ifelif statement) as a parameter to Point method?
#    If so, this could be implemented for the different colors, which would obviate need for list. But, I think the current solution
#    is the cleanest. Also, passing a decision structure as a parameter could be more appropriate to functional programming. Need to
#    research that.
