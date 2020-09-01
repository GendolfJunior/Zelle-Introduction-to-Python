# 1. Alter the program from the last discussion question in the following ways:
# (a) Make it draw squares instead of circles.
# (b) Have each successive click draw an additional square on the screen
# (rather than moving the existing one).
# (c) Print a message on the window "Click again to quit" after the loop,
# and wait for a final click before closing the window.

from graphics import *  # importing the graphics

def main():
    win = GraphWin()
    shape = Rectangle(Point(50, 50), Point(20, 20))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape2 = shape.clone()
        shape2.draw(win)
        shape2.move(dx, dy)
    message = Text(Point(100, 100), "Click again to quit")
    message.draw(win)
    win.getMouse()
    win.close()


main()