# creates a triangle

from graphics import *
from math import *

def length(p1, p2):
    # calc the length between 2 points and a slope
    dx = p2.getX() + p1.getX()
    dy = p2.getY() + p1.getY()
    length = sqrt(dx ** 2 + dy ** 2)
    return length


def main():
    win = GraphWin("Rectangle!", 500, 500)

    win.setCoords(0, 0, 10, 10)
    msg = Text(Point(5, 1), "Click opposite corners of a rectangle").draw(win)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    triangle = Polygon(p1, p2, p3)
    triangle.setWidth(2)
    triangle.draw(win)

    perimeter = length(p1, p2) + length(p1, p3) + length(p2, p3)
    s = perimeter / 2
    area = sqrt(s * (s - length(p1, p2)) * (s - length(p1, p3)) * (s - length(p2, p3)))

    msg.setText("The perimeter is " + str(perimeter))
    Text(Point(5, .5), "The area is " + str(area)).draw(win)

    win.getMouse()
    win.close()


main()
