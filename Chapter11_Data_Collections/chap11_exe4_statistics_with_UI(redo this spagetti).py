# 4. Give the program from the previous exercise (s) a graphical interface. You
# should have Entrys for the input and output file names and a button for
# each sorting order. Bonus: Allow the user to do multiple sorts and add a
# button for quitting.

from Chapter10_defining_classes.button import *
from Chapter11_Data_Collections.gpa import Student, makeStudent


def readStudents(filename):
    infile = open(filename, 'r')
    students = []
    for line in infile:
        students.append(makeStudent(line))
    infile.close()
    return students


def writeStudents(students, filename):
    outfile = open(filename, 'w')
    for s in students:
        print("{0}\t{1}\t{2}".format(s.getName(), s.getHours(), s.getQPoints()),
              file=outfile)
    outfile.close()


def quitOrPlay(win, quit, again):
    # Get a click in quit or again
    # Returns True if again clicked, false for quit
    quit.activate()
    again.activate()
    pt = win.getMouse()
    while not (quit.clicked(pt) or again.clicked(pt)):
        pt = win.getMouse()
    ans = again.clicked(pt)
    quit.deactivate()
    again.deactivate()
    return ans


def main():
    win = GraphWin("Students statistics", 400, 400)
    win.setCoords(0, 0, 100, 100)
    # list of text labels
    tSpecs = [(50, 90, "This program sorts student grade information"), (20, 80, "Input filename: "),
              (20, 70, "Output filename: "), (50, 60, "Pick a sorting field"), (50, 40, "Pick a sorting order")]
    # draw texts on the canvas
    texts = []
    for (cx, cy, label) in tSpecs:
        texts.append(Text(Point(cx, cy), label).draw(win))
    print(texts)
    # entry fields
    filenameEntry = Entry(Point(50, 80), 10)
    filenameEntry.draw(win)
    outfilename = Entry(Point(50, 70), 10)
    outfilename.draw(win)
    # buttons spec
    # available sorting fields and sorting order options
    bSpecs = [(25, 50, 15, 10, "Gpa"), (50, 50, 15, 10, "Name"), (75, 50, 15, 10, "Credits"),
              (25, 30, 25, 10, "Ascending"), (75, 30, 25, 10, "Descending"), (25, 10, 15, 10, "Quit"),
              (75, 10, 15, 10, "Read")]
    # draw all buttons on the canvas
    buttons = []
    for (cx, cy, width, height, label) in bSpecs:
        buttons.append(Button(win, Point(cx, cy), width, height, label))
    # activate all buttons
    for b in buttons:
        b.activate()
    win.getMouse()

    # get input data adn read content of input file
    data = readStudents(filenameEntry.getText())
    outfilename = outfilename.getText()
    # Waits for a button to be clicked
    # Returns the label of the button that was clicked
    while True:
        # loop for each mouse click
        click = win.getMouse()
        for b in buttons:
            # loop for each button
            if b.clicked(click):
                label = b.getLabel()
        if label == "Quit":  # method exit
            break
        choice = ''
        ochoice = ''
        while label != 'Quit' or label != 'Read':
            if label == 'Gpa':
                buttons[0].deactivate()
                choice = 'g'
            elif label == 'Name':
                buttons[1].deactivate()
                choice = 'n'
            elif label == 'Credits':
                buttons[2].deactivate()
                choice = 'c'
            if label != 'Ascending' or label != 'Descending':
                new_click_order = win.getMouse()
                label2 = ''
                for b2 in buttons:
                    # loop for each button
                    if b2.clicked(new_click_order):
                        label2 = b2.getLabel()
                    if label2 == 'Ascending':
                        buttons[3].deactivate()
                        ochoice = 'a'
                    elif label2 == 'Descending':
                        buttons[4].deactivate()
                        ochoice = 'd'
            else:
                if label == 'Ascending':
                    buttons[3].deactivate()
                    ochoice = 'a'
                elif label == 'Descending':
                    buttons[4].deactivate()
                    ochoice = 'd'
            if choice == 'n':
                print("Sorting by name.")
                data.sort(key=Student.getName)
            elif choice == 'c':
                print("Sorting by credits hours")
                data.sort(key=Student.getHours)
            else:
                print("Sorting by GPA.")
                data.sort(key=Student.gpa)
            if ochoice == 'd':
                print("Descending order")
                data.reverse()
            else:
                print("Ascending order")
            click = win.getMouse()
            for b in buttons:
                # loop for each button
                if b.clicked(click):
                    label = b.getLabel()
            if label == 'Read':
                buttons[6].deactivate()
                writeStudents(data, outfilename)
                print("The data has been written to", outfilename)


if __name__ == '__main__':
    main()
