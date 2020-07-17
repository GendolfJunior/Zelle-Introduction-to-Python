# You are to write a program that allows the user to draw a simple house using five mouse clicks.
# The first two clicks will be the opposite corners of the rectangular frame of the house.
# The third click will indicate the center of the top edge of a rectangular door.
# The door should have a total width that is 1/5 of the width of the house frame. The sides of the door should
# extend from the corners of the top down to the bottom of the frame. The fourth click will indicate the center of a square window.
# The window is half as wide as the door. The last click will indicate the peak of the roof.
# The edges of the roof will extend from the point at the peak to the corners of the top edge of the house frame.

# create canvas and set coordinates
# add intro text message on the canvas
# get click1 and click2, and draw a rectangular house
# get click3 for the door center
# calc the width and heights of the house
# calc the width of the door as 1/5 from the house width
# create 2 new points from the door top center
# draw a line of the door top
# get click4 is the center of the window
# draw a window
# get click5 and draw a poligon
from graphics import *


def main():
    win = GraphWin("Five-click House", 500, 500)
    win.setCoords(0, 0, 10, 10)
    message = Text(Point(5, 1), "Click 5 times to draw a house").draw(win)

    # drawing a rectangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    frame = Rectangle(p1, p2)
    frame.draw(win)
    # find length of rectangle sides a and b
    a = abs(p2.getX() - p1.getX())
    b = abs(p2.getY() - p1.getY())
    halfDoorwidth = (a / 10)

    #drawing a door
    p3 = win.getMouse()
    p3x = p3.getX()
    p3y = p3.getY()
    p3left = p3x - halfDoorwidth
    p3right = p3x + halfDoorwidth

    leftUpDoorCorner = Point(p3left, p3y)
    rightUpDoorCorner = Point(p3right, p3y)

    # drawing a door
    door_top = Line(leftUpDoorCorner, rightUpDoorCorner)
    door_top.draw(win)
    distanceTotop = p2.getY() - p3y
    doorHeights = b - distanceTotop
    leftBottomDoorCorner = Point(p3left, p3y - doorHeights)
    leftBottomDoorCorner.draw(win)
    rightBottomDoorCorner = Point(p3right, p3y - doorHeights)
    rightBottomDoorCorner.draw(win)
    leftLine = Line(leftUpDoorCorner, leftBottomDoorCorner).draw(win)
    rightLine = Line(rightUpDoorCorner, rightBottomDoorCorner).draw(win)

    # drawing a window
    p4 = win.getMouse()
    p4x = p4.getX()
    p4y = p4.getY()
   # p4.draw(win)
   # circ = Circle(p4, halfDoorwidth / 2)
    r = halfDoorwidth / 2
   # circ.draw(win)
    p4TopRight = Point(p4x + r, p4y + r)
    p4BottomLeft = Point(p4x - r, p4y - r)
    window = Rectangle(p4TopRight, p4BottomLeft)
    window.draw(win)

    # drawing a triangle
    p5 = win.getMouse()
    p6 = Point(p2.getX() - a, p2.getY())
    roof = Polygon(p5, p2, p6)
    roof.draw(win)

    win.getKey()
    win.close()

main()
