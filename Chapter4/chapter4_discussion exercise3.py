#  3.  Describe what happens when the following interactive graphics program runs:

from graphics import *  # importing the graphics


def main():                                     # defaining main function which will run everything
    win = GraphWin()                            # assigning to variable win a new object - window
    shape = Circle(Point(50, 50), 20)           # assigning to variable shape a new object circle with the center at x=50, y=50 and radius of 20
    shape.setOutline("red")                     # assigning property outline as red
    shape.setFill("red")                        # assigning property to fill the circle with red
    shape.draw(win)                             # it draws object circle into win object window
    for i in range(10):                         # get the user to click 10 times
        p = win.getMouse()                      # capture mouse position
        c = shape.getCenter()                   # aliasing shape central position
        dx = p.getX() - c.getX()                # subtract X coordinates of where user mouse clicked and position of shape
        dy = p.getY() - c.getY()                # subtract Y coordinates of where user mouse clicked and position of shape
        shape.move(dx, dy)                      # move the entire shape element to a new coordinates
    win.close()                                 # close the window when the loop is over


main()
