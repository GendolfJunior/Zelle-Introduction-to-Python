# 15. Write a program to plot a horizontal bar chart of student exam scores. Your program should get input from a file. The first line
#     of the file contains the count of the number of students in the file, and each subsequent line contains a student's last name
#     followed by a score in the range 0-100. Your program should draw a horizontal rectangle for each student where the length of the
#     bar represents the student's score. The bars should all line up on their left-hand edges.
#
#     Hint: Use the number of students to determine the size of the window and its coordinates. [Note to self: point of control.]
#     Bonus: label the bars at the left with the students' names.

# specification
# save in variable open the window where the file is
# save in variable open the file for reading
# read a first line into a variable count to calculate how many bars needed
# read starting from the second line all students into the list
# draw a window with coordinates relative to the quantity of students
# calculate a space required for a bar based on the students count and window size
# loop through the list of students
#       draw a bar with size student's rating
#       pass coordinates to the next iteration
from tkinter.filedialog import askopenfilename

from graphics import *


def main():
    print(
        "This program gets the text file with students rating as the input file\nreads each student rating an draws a horizontal barchart")

    # get the file name
    infilename = askopenfilename()
    infile = open(infilename, 'r')

    # get the first line with count of students
    count = int(infile.readline(1))
    print("There are {0} studetns in the file".format(count))

    #placeholder for student list
    students = []

    # read lines in the file except the first line with a count and strip off default EOL symbol in the end of each line
    for line in infile.readlines()[1:]:
        students.append(line[:-1])
        print(students)

    # draw a window with the size
    winHeight = 200 + 20 * count
    winWidth = 800
    print("The window Height size is, ", winHeight)

    win = GraphWin("Students rating", winWidth, winHeight)
    win.setCoords(0, 0, winWidth, winHeight)
    win.setBackground("grey")
    # 500 is used to scale as 100 points
    x = 500
    coef_x = 10
    Text(Point(x * 0 + coef_x, 10), "0").draw(win)
    Text(Point(x * 0.25 + coef_x, 10), "25").draw(win)
    Text(Point(x * 0.5 + coef_x, 10), "50").draw(win)
    Text(Point(x * 0.75 + coef_x, 10), "75").draw(win)
    Text(Point(x + 10, 10), "100").draw(win)

    # step between students
    step_y = (winHeight - 20) / count

    # draw bars
    y = 0
    for student in students:
        score = student.split(":")[1:]
        score = int(score[0]) / 100
        name = student.split(":")[0:1]
        name = str(name[0])
        bar = Rectangle(Point(10, y + 20), Point(x * score, y + 50))
        Text(Point(bar.getP2().getX() + 80, bar.getP2().getY() - 20), name).draw(win)
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)
        y += step_y

    # input("Press <any key> to quit")
    win.getKey()


main()
