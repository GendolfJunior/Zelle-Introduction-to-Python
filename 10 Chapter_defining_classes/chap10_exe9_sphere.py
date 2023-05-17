# 9. Write a class to represent spheres. Your class should implement the following
# methods:
# __init_(self, radius) Creates a sphere having the given radius.
# getRadius (self) Returns the radius of this sphere.
# surfaceArea(self) Returns the surface area of the sphere.
# volume (self) Returns the volume of the sphere.
# Use your new class to solve Programming Exercise 1 from Chapter 3.

from Chapter10_defining_classes.sphere import Sphere


def main():
    r = int(input("Enter a value of radius: "))
    new_sphere = Sphere(r)
    print("the Volume is: ", new_sphere.volume())
    print("The surface area is: ", new_sphere.surfaceArea())


if __name__ == '__main__':
    main()
