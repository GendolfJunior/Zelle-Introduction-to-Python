# 7. Write a modified Button class that creates circular buttons. Call your class
# CButton and implement the exact same methods that are in the existing
# Button class. Your constructor should take the center of the button
# and its radius as normal parameters. Place your class in a module called
# cbutton.py. Test your class by modifying roller.py to use your buttons.

# circular buttons.py

from math import *

from graphics import *


class CButton:
    """A button is a labeled circle in a window. It is activated or deactivated with the activate()
    and deactivate() methods . The clicked(p) method returns true if the button is active and if p is inside it."""

    def __init__(self, win, center, radius, label):
        """Creates a circular button , eg:
        qb = Button(myWin, centerPoint, center, radius, 'Quit')"""
        self.center = center
        self.radius = radius
        self.circle = Circle(center, radius)
        self.circle.setFill('lightgray')
        self.circle.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        "Returns true if button active and p is inside"
        return (self.active and
                sqrt(float((p.getX()) - float(self.center.getX())) ** 2 + (
                            float(p.getY()) - float(self.center.getY())) ** 2) < float(self.radius))

    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.circle.setWidth(2)
        self.active = True

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('darkgrey')
        self.circle.setWidth(1)
        self.active = False
