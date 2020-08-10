# 6. write a function that computes the area of a triangle given the length of its three sides as parameters (see programming exercise 9 from Chapter 3).
# Use your function to augment triangle2.py from this this chapter so that is also displays the area of the triangle.
#                                         s = (a + b + c) / 2
#                                         A = sqrt(s(s - a)(s - b)(s - c))
#
import math
from graphics import *


def are(a, b, c):
    s = (a + b + c) / 2  # half perimeter
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))  # area of a triangle (площа)
    return area


def square(x):
    return x ** 2


def distance(p1, p2):
    dist = math.sqrt(square(p2.getX() - p1.getX()) + square(p2.getY() - p1.getY()))
    return dist


def main():
    # a, b, c = eval(input("Enter three sides of triangle a, b, c: "))
    #    print("The area is: ", area(a, b, c))
    win = GraphWin("Draw a Triangle", 400, 400)
    win.setCoords(0.0, 0.0, 10, 10)
    message = Text(Point(5, 0.5), "Click on three points")
    message.draw(win)

    # Get and draw three vertices of triangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    # Use Polygon object to draw the triangle
    triangle = Polygon(p1, p2, p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)

    # Calculate the perimeter of the triangle
    a = distance(p1, p2)
    b = distance(p2, p3)
    c = distance(p3, p1)
    perim = a + b + c
    message.setText("The perimeter is: {0:0.2f}".format(perim))

    # calculate area of triangle
    tria_area = are(a, b, c)
    message2 = Text(Point(5, 1), "Area")
    message2.setText("The area is: {0:0.2f}".format(tria_area))
    message2.draw(win)

    # Wait for another click to exit
    win.getMouse()
    win.close()


main()
