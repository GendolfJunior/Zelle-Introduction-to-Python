#  4. Write a program that draws a winter scene with a Christmas tree and a snowman.

from graphics import *


def main():
    windowsize = 400
    win = GraphWin("Christmas tree and a snowman", windowsize, windowsize)
    win.setCoords(-100, -100, 100, 100)
    win.setBackground("gray")

    # christmas tree
    trunkTop = Point(0, 70)
    trunk1 = Line(Point(-10, -70), trunkTop)
    trunk1.draw(win)
    trunk2 = Line(Point(10, -70), trunkTop)
    trunk2.draw(win)
    # leaves
    upperLeft = Polygon(trunkTop, Point(-15, 50), Point(-10, 52), Point(-5, 54), Point(0, 56))
    upperLeft.draw(win)
    upperRight = Polygon(trunkTop, Point(15, 50), Point(10, 52), Point(5, 54), Point(0, 56))
    upperRight.draw(win)
    upperLeft2 = Polygon(Point(0, 56), Point(-18, 47), Point(-13, 48), Point(-8, 48), Point(0, 50))
    upperLeft2.draw(win)
    upperLeft3 = Polygon(Point(-36, 35), Point(-51, 3), Point(-36, 15))
    upperLeft3.draw(win)

    # Wait for another click to exit
    win.getMouse()
    win.close()


main()
