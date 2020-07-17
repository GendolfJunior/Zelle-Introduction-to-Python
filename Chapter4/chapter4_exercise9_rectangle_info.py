#  9. Rectangle Information.
#     This program displays information about a rectangle drawn by the user.
#     Input: Two mouse clicks for the opposite corners of a rectangle.
#     Output: Draw the rectangle.
#             Print the perimeter and area of the rectangle.
#     Formulas: area = (length)(width)
#               perimeter = 2(length + width)
from graphics import *
from math import *


def main():
    # draw a canvas and coordinate system
    win = GraphWin("Rectangle information", 400, 400)
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    win.setBackground("grey")

    # draw a text message "click 2 times on the canvas"
    message = Text(Point(5, 1), "click 2 times on the canvas\n to draw a rectangle")
    message.draw(win)

    # get clicks, get click coordinates and draw points
    click1 = win.getMouse()
    point1 = Point(click1.getX(), click1.getY())
    point1Circle = Circle(point1, 0.1)
    point1Circle.setFill("red")
    point1Circle.draw(win)

    click2 = win.getMouse()
    point2 = Point(click2.getX(), click2.getY())
    point2Circle = Circle(point2, 0.1)
    point2Circle.setFill("red")
    point2Circle.draw(win)

    rect = Rectangle(point1, point2)
    rect.setOutline("blue")
    rect.setFill("cyan")
    rect.draw(win)
    message.undraw()

    #calc perimeter and area
    perim = ceil(2 * (abs(click2.getX() - click1.getX()) + abs(click2.getY() - click1.getY())))
    area = ceil((abs(click2.getX() - click1.getX())) * (abs(click2.getY() - click1.getY())))
    print('Point 1 coordinates are: ', point1)
    print('Point 2 coordinates are: ', point2)
    print("Width is: ", abs(click2.getX() - click1.getX()))
    print("Heights is: ", abs(click2.getY() - click1.getY()))


    message = Text(Point(5, 1), "The perimeter is {0} and the area is {1}".format(perim, area))
    message.draw(win)

    #exit the program
    win.getKey()
    win.close()


main()
