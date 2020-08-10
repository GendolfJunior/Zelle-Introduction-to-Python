# 16. Archery Scorer. Write a program that draws an archery target (see Programming
# Exercise 2 from Chapter 4) and allows the user to click five
# times to represent arrows shot at the target. Using five-band scoring, a
# bulls-eye (yellow) is worth 9 points and each successive ring is worth 2
# fewer points down to 1 for white. The program should output a score for
# each click and keep track of a running sum for the entire series.

# algorithm
# draw a Canvas 400 x 400
# draw a target with Circles as in chap4_exe2
# create a running sum score and count of clicks. Set them to 0
# create while loop for 5 user clicks
# create a function that accepts user click and returns the distance from the center to the point beased on the point coordinates
# create a function that accepts distanace to point and based on number and returns a score
# update count of clicks and update count running total sum of points

from math import *

from graphics import *


def createCircle(win, center, width, color):
    circle = Circle(center, width)
    circle.setFill(color)
    circle.draw(win)
    return circle


def distanceToPoint(pt, center):
    distance = sqrt(((pt.getX() - center.getX()) ** 2 + (pt.getY() - center.getY()) ** 2))
    return distance


def calcScore(ptDistance, width):
    score = 9
    if ptDistance <= width:
        score
    elif width * 2 >= ptDistance > width:
        score -= 2
    elif width * 3 >= ptDistance > width * 2:
        score -= 4
    elif width * 4 >= ptDistance > width * 3:
        score -= 6
    elif width * 5 >= ptDistance > width * 4:
        score -= 8
    else:
        score = 0
    return score


def main():
    win = GraphWin("Archery Target chapter 7 exe 16", 400, 400)
    win.setBackground("grey")
    center = Point(200, 200)
    width = 25
    colorW, colorB, colorBL, colorR, colorY = 'white', 'black', 'blue', 'red', 'yellow'
    circleW = createCircle(win, center, width * 5, colorW)
    circleB = createCircle(win, center, width * 4, colorB)
    circleBl = createCircle(win, center, width * 3, colorBL)
    circleR = createCircle(win, center, width * 2, colorR)
    circleY = createCircle(win, center, width, colorY)

    countClicks = 0
    sumPoints = 0
    while countClicks < 5:
        pt = win.getMouse()
        ptDistance = distanceToPoint(pt, center)
        ptScore = calcScore(ptDistance, width)
        sumPoints += ptScore
        countClicks += 1

    print("the total score is: ", sumPoints)
    # Wait for 5 clicks to exit
    win.close()


if __name__ == '__main__':
    main()
