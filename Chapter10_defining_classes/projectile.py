# projectile.py

"""projectile.py
Provides a simple class for modeling the flight of projectiles."""

from math import pi, sin, cos

from .button import *
from graphics import *


class Projectile:
    """Simulates the flight of simple projectiles near the earth's
    surface, ignoring wind resistance. Tracking is done in two
    dimensions, height (y) and distance (x)."""

    def __init__(self, angle, velocity, height):
        """Create a projectile with given launch angle, initial
        velocity and height."""
        self.xpos = 0.0
        self.ypos = height
        theta = pi * angle / 180.0
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)

    def update(self, time):
        """Update the state of this projectile to move it time seconds
        farther into its flight"""
        self.xpos = self.xpos + time * self.xvel
        yvel1 = self.yvel - 9.8 * time
        self.ypos = self.ypos + time * (self.yvel + yvel1) / 2.0
        self.yvel = yvel1

    def getY(self):
        """Returns the y position (height) of this projectile."""
        return self.ypos

    def getX(self):
        """Returns the x position (distance) of this projectile."""
        return self.xpos


class ShotTracker:
    def __init__(self, win, angle, velocity, height):
        """win is the GraphWin to display the shot . angle, velocity, and height are initial projectile parameters."""
        self.proj = Projectile(angle, velocity, height)
        self.marker = Circle(Point(0, height), 3)
        self.marker.setFill("red")
        self.marker.setOutline("red")
        self.marker.draw(win)

    def update(self, dt):
        """Move the shot dt seconds farther along its flight"""
        # update the projectile
        self.proj.update(dt)
        # move the circle to the new projectile location
        center = self.marker.getCenter()
        dx = self.proj.getX() - center.getX()
        dy = self.proj.getY() - center.getY()
        self.marker.move(dx, dy)

    def getX(self):
        """return the current x coordinate of the shot's center"""
        return self.proj.getX()

    def getY(self):
        """"return the current y coordinate of the shot's center"""
        return self.proj.getY()

    def undraw(self):
        """"undraw the shot"""
        self.marker.undraw()


class InputDailog:
    """A custom window for getting simulation values (angle, velocity, and height) from the user."""

    def __init__(self, angle, vel, height):
        """ Build and display the input window """
        self.win = win = GraphWin("Initial Values", 200, 300)
        win.setCoords(0, 4.5, 4, .5)

        Text(Point(1, 1), "Angle").draw(win)
        self.angle = Entry(Point(3, 1), 5).draw(win)
        self.angle.setText(str(angle))

        Text(Point(1, 2), "Velocity").draw(win)
        self.vel = Entry(Point(3, 2), 5).draw(win)
        self.vel.setText(str(vel))

        Text(Point(1, 3), "Height").draw(win)
        self.height = Entry(Point(3, 3), 5).draw(win)
        self.height.setText(str(height))

        self.fire = Button(win, Point(1, 4), 1.25, .5, "Fire ! ")
        self.fire.activate()

        self.quit = Button(win, Point(3, 4), 1.25, .5, "Quit")
        self.quit.activate()

    def interact(self):
        """ wait for user to click Quit or Fire button
        Returns a string indicating which button was clicked """

        while True:
            pt = self.win.getMouse()
            if self.quit.clicked(pt):
                return "Quit"
            if self.fire.clicked(pt):
                return "Fire!"

    def getValues(self):
        a = float(self.angle.getText())
        v = float(self.vel.getText())
        h = float(self.height.getText())
        return a, v, h

    def close(self):
        """ close the input window"""
        self.win.close()
