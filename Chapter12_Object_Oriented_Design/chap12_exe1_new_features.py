# 1. Modify the Dice Poker program from this chapter to include any or all of
# the following features:
#       a) Splash Screen. When the program first fires up, have it print a short
#           introductory message about the program and buttons for "Let's Play''
#           and "Exit." The main interface shouldn't appear unless the user selects "Let's Play."
#       b) Add a "Help" button that pops up another window displaying the
#           rules of the game (the payoffs table is the most important part).
#       c) Add a high score feature. The program should keep track of the 10
#           best scores. When a user quits with a good enough score, he/she is
#           invited to type in a name for the list. The list should be printed in
#           the splash screen when the program first runs. The high-scores list
#           will have to be stored in a file so that it persists between program invocations.

from Chapter12_Object_Oriented_Design.chapter12_code.button import Button
from Chapter12_Object_Oriented_Design.chapter12_code.cdieview import ColorDieView
from Chapter12_Object_Oriented_Design.chapter12_code.graphics import *
from Chapter12_Object_Oriented_Design.chapter12_code.pokerapp import PokerApp


class GraphicsInterface:

    def __init__(self):
        self.win = GraphWin("Dice Poker", 600, 400)
        self.win.setBackground("green3")
        banner = Text(Point(300, 30), "Python  Poker  Parlor")
        banner.setSize(24)
        banner.setFill("yellow2")
        banner.setStyle("bold")
        banner.draw(self.win)
        self.msg = Text(Point(300, 380), "Welcome to the Dice Table")
        self.msg.setSize(18)
        self.msg.draw(self.win)

        # this is a method to display a splash screen
        self.splashScreen(self.win)

        self.createDice(Point(300, 100), 75)
        self.buttons = []
        self.addDiceButtons(Point(300, 170), 75, 30)
        # help button
        b = Button(self.win, Point(25, 375), 40, 30, "Help")
        self.buttons.append(b)
        b = Button(self.win, Point(300, 230), 400, 40, "Roll Dice")
        self.buttons.append(b)
        b = Button(self.win, Point(300, 280), 150, 40, "Score")
        self.buttons.append(b)
        b = Button(self.win, Point(570, 375), 40, 30, "Quit")
        self.buttons.append(b)
        self.money = Text(Point(300, 325), "$100")
        self.money.setSize(18)
        self.money.draw(self.win)

    # def splash prompts user to start the game
    def splashScreen(self, win):
        exitWindow = Button(self.win, Point(280, 300), 40, 30, "Quit")
        exitWindow.activate()
        play = Button(self.win, Point(330, 300), 40, 30, "Play")
        play.activate()
        p = Point(0, 0)
        while not play.clicked(p):
            if exitWindow.clicked(p):
                self.win.close()
            else:
                p = self.win.getMouse()
                if play.clicked(p):
                    play.removeButton()
                    exitWindow.removeButton()

    # this function shows the help screen to the user
    def helpScreen(self):
        win2 = GraphWin("Game help", 800, 300)
        win2.setCoords(0, 0, 100, 100)
        win2.setBackground("grey")
        help = 'This game of dice poker allows the user to roll for hands "(5-3)-of-a-kind",\
        \n"Full House", "Straight", etc. Each round consists of up to three rolls. the user\n \
        will select the appropriate dice to re-roll. If no dice are chosen, the user will be scored\
        \n based on the initial roll.\n'
        payouts = "{0:<100}{1:>0}\n------------------------------\
        --------------------------------\n".format("Hands", "Pay")
        hand_specs = [("Two Pairs", 5), ("Three of a Kind", 8), ("Full House", 12), ("Four of a Kind", 15),
                      ("Straight (1-5 or 2-6)", 20), ("Five of a Kind", 30)]
        for (hand, pay) in hand_specs:
            payouts = payouts + '{0:<100} ${1:>0.2f}\n'.format(hand, pay)
        msg = Text(Point(50, 20), help)
        msg.setSize(11)
        msg2 = Text(Point(50, 60), payouts)
        msg.draw(win2)
        msg2.draw(win2)
        win2.getMouse()
        win2.close()


    def createDice(self, center, size):
        center.move(-3 * size, 0)
        self.dice = []
        for i in range(5):
            view = ColorDieView(self.win, center, size)
            self.dice.append(view)
            center.move(1.5 * size, 0)

    def addDiceButtons(self, center, width, height):
        center.move(-3 * width, 0)
        for i in range(1, 6):
            label = "Die {0}".format(i)
            b = Button(self.win, center, width, height, label)
            self.buttons.append(b)
            center.move(1.5 * width, 0)

    def setMoney(self, amt):
        self.money.setText("${0}".format(amt))

    def showResult(self, msg, score):
        if score > 0:
            text = "{0}! You win ${1}".format(msg, score)
        else:
            text = "You rolled {0}".format(msg)
        self.msg.setText(text)

    def setDice(self, values):
        for i in range(5):
            self.dice[i].setValue(values[i])

    def wantToPlay(self):
        ans = ''
        while ans != "Quit":
            ans = self.choose(["Roll Dice", "Quit", "Help"])
            self.msg.setText("")
            if ans == "Help":
                self.helpScreen()
            else:
                return ans == "Roll Dice"

    def close(self):
        self.win.close()

    def chooseDice(self):
        # choices is a list of the indexes of the selected dice
        choices = []  # No dice chosen yet
        while True:
            # wait for user to click a valid button
            b = self.choose(["Die 1", "Die 2", "Die 3", "Die 4", "Die 5",
                             "Roll Dice", "Score"])

            if b[0] == "D":  # User clicked a die button
                i = int(b[4]) - 1  # Translate label to die index
                if i in choices:  # Currently selected, unselect it
                    choices.remove(i)
                    self.dice[i].setColor("black")
                else:  # Currently unselected, select it
                    choices.append(i)
                    self.dice[i].setColor("gray")
            else:  # User clicked Roll or Score or Help
                for d in self.dice:  # Revert appearance of all dice
                    d.setColor("black")
                if b == "Score":  # Score clicked, ignore choices
                    return []
                if b == "Help":  # user wants to see User help
                    return self.helpScreen()
                elif choices != []:  # Don't accept Roll unless some
                    return choices  # dice are actually selected

    def choose(self, choices):
        buttons = self.buttons

        # activate choice buttons, deactivate others
        for b in buttons:
            if b.getLabel() in choices:
                b.activate()
            else:
                b.deactivate()

        # get mouse clicks until an active button is clicked
        while True:
            p = self.win.getMouse()
            for b in buttons:
                if b.clicked(p):
                    return b.getLabel()  # function exit here.


def main():
    inter = GraphicsInterface()
    app = PokerApp(inter)
    app.run()


if __name__ == '__main__':
    main()
