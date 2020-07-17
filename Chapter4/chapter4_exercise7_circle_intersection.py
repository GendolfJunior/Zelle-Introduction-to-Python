#  7. Circle Intersection.
#     Write a program that computes the intersection of a circle with a horizontal line and displays the information textually and graphically.
#     Input: Radius of the circle and the y-intercept of the line.
#     Output: Draw a circle centered at (0,0) with teh given radius in a window with coordinates running from -10,-10 to 10,10.
#     Draw a horizontal line across the window and the given-y intercept.
#     Draw the two points of intersection in red.
#     Print out the x values of the points of intersection.
#     Formula: x = + or -(sqrt((r^2 = y^2)))

from math import *

# draw a canvas 400 x 400
# set the coordinate system in the canvas to -10, -10, 10, 10
# get user input of radius
# get user input of y-intercept line
# draw a circle at (0, 0)
# draw a line
# draw 2 points of intersection in red
# print out the x values
from graphics import *


def main():
    # user inputs
    r = int(input("Enter radius of a circle in a range from (0, 10]: "))
    y = int(input("Enter y-intercept coordinate which is less then radius: "))
    # draw a canvas
    win = GraphWin("Circle Interception", 400, 400)
    win.setCoords(-10, -10, 10, 10)

    # draw a circle
    circle = Circle(Point(0, 0), r)
    circle.draw(win)

    # calc horizontal line x coordinates
    x1 = sqrt(r ** 2 - y ** 2)
    x2 = -sqrt(r ** 2 - y ** 2)
    print(str(x1), str(x2))

    # construct points
    point1 = Point(x1, y)
    point1.setFill("red")
    point1.draw(win)
    point2 = Point(x2, y)
    point2.setFill("red")
    point2.draw(win)

    # draw horizontal line
    horizontal_line = Line(Point(-10, y), Point(10, y))
    horizontal_line.draw(win)

    # draw circles as bog points
    point1_circle = Circle(point1, 0.1)
    point1_circle.setFill("red")
    point1_circle.draw(win)
    point2_circle = Circle(point2, 0.1)
    point2_circle.setFill("red")
    point2_circle.draw(win)

    win.getMouse()
    win.close()


main()
