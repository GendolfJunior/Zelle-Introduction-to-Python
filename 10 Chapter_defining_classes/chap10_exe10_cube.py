# 10. Same as the previous problem, but for a cube. The constructor should
# accept the length of a side as a parameter.

class Cube:

    def __init__(self, sideLength):
        self.sideLength = sideLength

    def getSideLength(self):
        return self.sideLength

    def surfaceArea(self):
        self.cubeSurface = 6 * self.sideLength ** 2
        return self.cubeSurface

    def volume(self):
        self.cubeVolume = self.sideLength ** 3
        return self.cubeVolume


def main():
    side = int(input("Enter a value of cube side length: "))
    new_cube = Cube(side)
    print("the Volume is: ", new_cube.volume())
    print("The surface area is: ", new_cube.surfaceArea())


if __name__ == '__main__':
    main()
