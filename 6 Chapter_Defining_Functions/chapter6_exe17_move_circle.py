# 17. Write a function to meet this specification.
#   moveTo(shape, newCenter) shape is a graphics object that supports the
#   getCenter method and newCenter is a Point. Moves shape so that
#   newCenter is its center.
# Use your function to write a program that draws a circle and then allows
# the user to click the window 10 times. Each time the user clicks, the circle
# is moved where the user clicked.


from graphics import *


def moveTo(shape, newCenter):
    center = shape.getCenter()
    dx = newCenter.getX() - center.getX()
    dy = newCenter.getY() - center.getY()
    shape.move(dx, dy)


def main():
    print("this program draws a circle and moves it around")
    win = GraphWin("Move object", 400, 400)
    win.setCoords(-10, -10, 10, 10)

    # draw a circle
    click = win.getMouse()
    circle = Circle(click, 2)
    circle.draw(win)

    for i in range(10):
        newCenter = win.getMouse()
        moveTo(circle, newCenter)

    win.getMouse()
    win.close()


main()
