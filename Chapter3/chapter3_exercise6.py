#  6. Two points in a plane are specified using the coordinates (x1,y1) and (x2,y2). Write a program that calculates the slope of a line through
#     two (non-vertical) points entered by the user.
#                                                   slope = (y2 - y1) / (x2 - x1)

def main():
    x1, y1 = eval(input("enter x1 and y1, using comma ',' as a separator : "))
    x2, y2 = eval(input("enter x2 and y2, using comma ',' as a separator : "))
    slope = (y2 - y1) / (x2 - x1)
    print("The slope is: ", slope)


main()
