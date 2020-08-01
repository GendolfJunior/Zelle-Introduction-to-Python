#  15. Do Programming Exercise 8 from Chapter 4, but add a decision to prevent
# the program from dividing by zero if the line is vertical.
#  8. Line Segment Information.
#     This program allows the suer to draw a line segment that then displays some graphical and textual information about the line segment.
#     Input: Two mouse clicks for the end points of the line segment.
#     Output: Draw the midpoint of the segment in cyan.
#             Draw the line.
#             Print the length and the slope of the line.
#     Formulas: dx = x2 - x1
#               dy = y2 - y1
#               slope = dy / dx
#               length = sqrt(dx^2 + dy^2)

# initiate a canvas object with a name like exercise name and size 400 x 400
# get user 2 clicks and save them in 2 variables
# get the coordinates of each click
# draw a Point for each click
# draw a mid point
# calculate the distance between coordinates, slope and length
# print out the length and the slope of the line

from math import *

from graphics import *


def clicks(win):
    # get a click and draw it
    click = win.getMouse()
    point = Point(click.getX(), click.getY())
    point.setFill("red")
    point.setOutline("red")
    point.draw(win)
    return click, point


def midpoint(win, click1, click2):
    # it draws a midpoint on the line
    mx = (click2.getX() + click1.getX()) / 2
    my = (click2.getY() + click1.getY()) / 2
    midpoint = Point(mx, my)
    midpoint.setFill("cyan")
    midpoint.setOutline("cyan")
    midpoint.draw(win)


def main():
    win = GraphWin("Line Segment Information", 400, 400)
    win.setBackground("grey")
    win.setCoords(-10, -10, 10, 10)

    # get clicks, get click coordinates and draw points
    click1, point1 = clicks(win)
    click2, point2 = clicks(win)

    # draw a midpoint
    midpoint(win, click1, click2)

    # draw a line
    li = Line(point1, point2)
    li.draw(win)

    # calc the length between 2 points and a slope
    dx = click2.getX() + click1.getX()
    dy = click2.getY() + click1.getY()

    if dx != 0.0:
        slope = dy / dx
        length = sqrt(dx ** 2 + dy ** 2)
        print("Point 1 coordinates: ", point1)
        print("Point 2 coordinates: ", point2)
        print("Mid Point coordinates: ", midpoint)
        print("The length is {0} is coordinates".format(length))
        print("The slope is {0}".format(slope))
    else:
        print("division by 0 is not allowed")

    win.getKey()
    win.close()


main()
