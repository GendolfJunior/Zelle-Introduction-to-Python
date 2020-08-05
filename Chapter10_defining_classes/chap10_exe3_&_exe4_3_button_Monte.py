# 3. Write a program to play "Three Button Monte." Your program should draw three buttons labeled "Door 1", "Door 2" and "Door 3" in a window and
# randomly select one of the buttons (without telling the user which one is selected). The program then prompts the user to click on one of the
# buttons. A click on the special button is a win, and a click on one of the other two is a loss. You should tell the user whether they won or lost, and
# in the case of a loss, which was the correct button. Your program should be entirely graphical; that is, all prompts and messages should be displayed
# in the graphics window.

# 4. Extend the program from the previous problem by allowing the player to
# play multiple rounds and displaying the number of wins and losses. Add a
# "Quit" button for ending the game.

# I accidentally straight away have implemented exercise #4 while doing #3

from random import *

from Chapter10_defining_classes.button import *


class Door:
    def __init__(self):
        # create animation window
        self.win = GraphWin("3 buttons Monte", 420, 420)
        self.win.setCoords(0, 0, 200, 200)
        # create buttons
        self.guess = randint(1, 3)
        self.button1 = Button(self.win, Point(100, 160), 45, 30, "Door\n1")
        self.button1.activate()
        self.button2 = Button(self.win, Point(100, 100), 45, 30, "Door\n2")
        self.button2.activate()
        self.button3 = Button(self.win, Point(100, 40), 45, 30, "Door\n3")
        self.button3.activate()
        self.quit = Button(self.win, Point(30, 40), 45, 30, "Quit")
        self.quit.activate()

    def assign_guess(self):
        return self.guess

    def interact(self):
        """ wait for user to click Quit or one of 3 buttons
        Returns a string indicating which button was clicked """

        while True:
            pt = self.win.getMouse()
            if self.quit.clicked(pt):
                return "Quit"
            if self.button1.clicked(pt):
                return 1
            if self.button2.clicked(pt):
                return 2
            if self.button3.clicked(pt):
                return 3

    def close(self):
        """ close the input window"""
        self.win.close()

    def dialog(self, text, answer):
        """pop-up window with a result. Click Ok to close it """
        self.dial = GraphWin("Answer", 210, 210)
        self.dial.setCoords(0, 0, 100, 100)
        Text(Point(55, 70), text).draw(self.dial)
        Text(Point(55, 45), "the guess was: " + str(answer)).draw(self.dial)
        self.buttonOK = Button(self.dial, Point(10, 10), 20, 15, 'OK')
        self.buttonOK.activate()
        pt = self.dial.getMouse()
        if self.buttonOK.clicked(pt):
            self.dial.close()


def main():
    while True:
        simulate = Door()
        door_guessed = simulate.assign_guess()
        choice = simulate.interact()
        if choice == "Quit":  # loop exit
            break
        if choice == door_guessed:
            simulate.dialog("Your guess is correct!", door_guessed)
        else:
            simulate.dialog("Your guess is incorrect!", door_guessed)

        # close up shop
        simulate.close()


if __name__ == '__main__':
    main()
