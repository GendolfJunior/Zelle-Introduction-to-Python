# 16 Use your drawFace function from the previous exercise to write a photo
# anonymizer. This program allows a user to load an image file (such as a
# PPM or GIF) and to draw cartoon faces over the top of existing faces in the
# photo. The user first inputs the name of the file containing the image. The
# image is displayed and the user is asked how many faces are to be blocked.
# The program then enters a loop for the user to click on two points for each
# face: the center and somewhere on the edge of the face (to determine the
# size of the face) . The program should then draw a face in that location
# using the drawFace function.

# Hints: Section 4.8.4 describes the image-manipulation methods in the
# graphics library. Display the image centered in a GraphWin that is the same
# width and height as the image, and draw the graphics into this window.
# You can use a screen capture utility to save the resulting images.e


from math import *

from graphics import *


def drawFace(center, size, window):
    eyeSize = 0.15 * size
    eyeOff = size / 3.0
    mouthSize = 0.8 * size
    mouthOff = size / 2.0
    head = Circle(center, size)
    head.setFill("yellow")
    head.draw(window)
    leftEye = Circle(center, eyeSize)
    leftEye.move(eyeOff, eyeOff)
    rightEye = Circle(center, eyeSize)
    rightEye.move(-eyeOff, eyeOff)
    leftEye.draw(window)
    rightEye.draw(window)
    p1 = center.clone()
    p1.move(mouthSize / 2, -mouthOff)
    p2 = center.clone()
    p2.move(-mouthSize / 2, -mouthOff)
    mouth = Line(p1, p2)
    mouth.draw(window)


def loadImage(picFile):
    loadedImage = Image(Point(0, 0), picFile)
    windowWidth = loadedImage.getWidth()
    windowHeights = loadedImage.getHeight()
    win = GraphWin(picFile, windowWidth, windowHeights)
    win.setCoords(-10, -10, 10, 10)
    loadedImage.draw(win)
    return win


def sizeCalc(win):
    # this function gets user input as 2 clicks and calculates the length of the vector
    p1 = win.getMouse()
    p2 = win.getMouse()
    radius = sqrt((p2.getX() - p1.getX()) ** 2 + (p2.getY() - p1.getY()) ** 2)
    return radius, p1


def test():
    print("Photo Anonymizer: Draw faces over pictures.")
    picFile = input("Enter name of file containing GIF or PPM formats image: ")
    faces = int(input("How many faces there? "))
    win = loadImage(picFile)

    # loop over the number of faces on the photo
    for i in range(faces):
        size, center = sizeCalc(win)
        print(size, center)
        drawFace(center, size, win)

    win.getMouse()
    win.close()


test()
