# 16. Write a program to draw a quiz score histogram. Your program should read data from a file. Each line of the file contains a number
#     in the range 0-10. Your program must count the number of occurences of each score and then draw a vertical bar chart with a bar for
#     each possible score (0-10) with height corresponding to the count of that score. For example, if 15 students got an 8, then the
#     the height of the bar for 8 should be 15.
#     Hint: Use a list that stores the count for each possible score.

#     1. Problem analysis:
#        How to count number of occurences of possible test scores and represent the count on a vertical chart.
#
#     2. Specification:
#        Inputs: file with test scores
#        Output: histogram representing occurences of each score
#
#     3. Design (algorithm)
#        import graphics library
#        import dialog box for opening file
#        get the file name
#        open the file
#        read file
#        create empty list for scores
#        process each line of the input file
#        get each score
#        append each score to empty list in output file
#        count the number of occurences of each score
#        store each count in a new list
#        create graphical template for histogram using a loop
#        define one rectangle (bar) and use variable for height
#        define space between bars as equal to width of one bar
#        label each bar from 0 to 10 using loop count
#        use
#
#     4. Implement
#
# use file 'scores'


from tkinter.filedialog import askopenfilename
from graphics import *


def file():
    # get the input filename and open it for reading
    inFilname = askopenfilename()
    infile = open(inFilname, 'r')
    return infile


def score(infile):
    # create a list of score values as integers
    scores = []
    for score in infile.readlines():
        scores.append(int(score[:-1]))
    scores.sort()
    print(scores)
    return scores


def score_count(scores):
    score_counts = []
    # loop through the range of 0 to 10
    for i in range(11):
        # count occurances of each i sequence number
        score_count = scores.count(i)
        # form a new list with maximum items equal to the range 10 and add count of occurances
        score_counts.append(score_count)
        # score_counts.append([i, scores.count(i)])
    return score_counts

def x_labes(x_bar_start, win, x_bar_step):
    # draw the labels for X axis
    for i in range(11):
        Text(Point(x_bar_start, 10), i).draw(win)
        x_bar_start += x_bar_step

def main():
    print("This program reads a file with scores and calculates an occurance of each score")
    infile = file()
    scores = score(infile)

    # how many scores of students in the file
    students_count = len(scores)
    print("students count of scores is: ", students_count)

    score_counts = score_count(scores)
    print(score_counts)

    # draw a window with the given size and set coordinates, and background
    winHeight = 200 + 20 * students_count
    winWidth = 1000
    max_bar_height = 30 * students_count
    print("The window Height is, ", winHeight)
    print("The window Width is, ", winWidth)
    win = GraphWin("Students scores count", winWidth, winHeight)
    win.setCoords(0, 0, winWidth, winHeight)
    win.setBackground("grey")

    # draw axis X labels
    x_start = 40
    x_bar_step = 90
    x_labes(x_start, win, x_bar_step)
    y_start = 20

    # draw bars with count of scores
    for i in score_counts:
        score_relative = i / students_count
        point1 = Point(x_start - 30, y_start)
        point2 = Point(x_start + 30, y_start + max_bar_height * score_relative)
        bar = Rectangle(point1, point2)
        bar.setFill("blue")
        bar.setWidth(2)
        bar.draw(win)
        x_start += x_bar_step

    # input("Press <any key> to quit")
    win.getKey()


main()
