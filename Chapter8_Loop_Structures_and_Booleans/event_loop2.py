# event_loop2.py --- color-changing window

from graphics import *


def handleKey(k, win):
    if k == "r":
        win.setBackground("pink")
    elif k == "w":
        win.setBackground("white")
    elif k == "g":
        win.setBackground("lightgray")
    elif k == "b":
        win.setBackground("lightblue")


def handleClick(pt, win):
    # create an Entry for user to type in
    entry = Entry(pt, 10)
    entry.draw(win)
    # Go modal: loop until user types <Enter> key
    while True:
        key = win.getKey()
        if key == "Return": break
    # undraw the entry and create and draw TextO
    entry.undraw()
    typed = entry.getText()
    Text(pt, typed).draw(win)
    # clear (ignore) any mouse click that occurred during text entry
    win.checkMouse()


def main():
    win = GraphWin("Click and Type", 500, 500)
    # Event Loop: handle key presses and mouse clicks until the user
    # presses the "q" key.
    while True:
        key = win.checkKey()
        if key == 'q':  # loop exit
            break

        if key:
            handleKey(key, win)

        pt = win.checkMouse()
        if pt:
            handleClick(pt, win)

    win.close()


main()
