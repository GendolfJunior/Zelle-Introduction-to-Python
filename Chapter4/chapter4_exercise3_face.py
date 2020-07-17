# 3. Write a program that draws some sort of face.

from graphics import *


def main():
    windowsize = 400
    win = GraphWin("Some face", windowsize, windowsize)
    win.setCoords(-10, -10, 10, 10)
    win.setBackground("gray")
    center = Point(0, 0)
    ax = -5
    ay = 6
    eyesRadius = 0.5

    # drawing a face oval
    faceoval = Oval(Point(ax, ay), Point(-ax, -ay))
    faceoval.setFill("white")
    faceoval.draw(win)

    # drawing eyes
    # c = sqrt(a^2 + b^2)
    # c = sqrt(ax ** 2 + ay ** 2)
    # print("'c' is: ", c)
    l = Line(Point(ax, 0), Point(0, ay))
    lx = l.getCenter().getX()
    ly = l.getCenter().getY()
    leftEye = Circle(Point(lx + 0.5, ly - 1), eyesRadius)
    leftEye.setFill("cyan")
    rightEye = Circle(Point(-lx - 0.5, ly - 1), eyesRadius)
    rightEye.setFill("cyan")
    leftEye.draw(win)
    rightEye.draw(win)

    # eyebowls
    leftEyeBowl = Circle(leftEye.getCenter(), eyesRadius / 2)
    rightEyeBowl = Circle(rightEye.getCenter(), eyesRadius / 2)
    leftEyeBowl.setFill("black")
    rightEyeBowl.setFill("black")
    leftEyeBowl.draw(win)
    rightEyeBowl.draw(win)

    # drawing mouse
    mousePoint1x = leftEye.getCenter().getX()
    mousePoint1y = -leftEye.getCenter().getY()
    mousePoint2x = rightEye.getCenter().getX()
    mousePoint2y = -rightEye.getCenter().getY()
    mouse = Oval(Point(mousePoint1x, mousePoint1y), Point(mousePoint2x, mousePoint2y - 0.5))
    mouse.draw(win)

    # draw a nose
    noseVerticalPointX = center.getX()
    noseVerticalPoint1y = center.getY() + 1
    noseVerticalPoint2y = center.getY() - 0.5

    nose = Line(Point(noseVerticalPointX, noseVerticalPoint1y), Point(noseVerticalPointX, noseVerticalPoint2y))
    noseBottom = Oval(Point(noseVerticalPointX - 0.5, noseVerticalPoint2y), Point(noseVerticalPointX + 0.5, noseVerticalPoint2y - 0.5))

    nose.draw(win)
    noseBottom.draw(win)

    # Wait for another click to exit
    win.getMouse()
    win.close()


main()
