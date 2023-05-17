# 9. Write a class to represent spheres. Your class should implement the following
# methods:
# __init_(self, radius) Creates a sphere having the given radius.
# getRadius (self) Returns the radius of this sphere.
# surfaceArea(self) Returns the surface area of the sphere.
# volume (self) Returns the volume of the sphere.
# Use your new class to solve Programming Exercise 1 from Chapter 3.

from math import *


class Sphere:

    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

    def surfaceArea(self):
        self.surface = 4 * pi * self.radius ** 2
        return self.surface

    def volume(self):
        self.volume = 4.0 / 3.0 * pi * self.radius ** 3
        return self.volume
