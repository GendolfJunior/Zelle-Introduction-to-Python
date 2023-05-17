# 12. Extend your card class from the previous problem with a draw(self, win, center) method that displays the card in a graphics window.
# Use your extended class to create and display a hand of five random cards.
# Hint: The easiest way to do this is to search the Internet for a free set of
# card images and use the Image object in the graphics library to display them.

from random import randrange
from graphics import *
from Chapter10_defining_classes.Playing_Card_Images import *

class PlayingCard:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def value(self):
        if self.getRank() < 10:
            return self.rank
        else:
            return 10

    def __str__(self):
        ranks = [None, "Ace", "Two", "Three", "Four", "Five", "Six",
                 "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
        rankStr = ranks[self.rank]

        if self.suit == 'c':
            suitStr = "Clubs"
        elif self.suit == 'd':
            suitStr = "Diamonds"
        elif self.suit == 'h':
            suitStr = "Hearts"
        else:
            suitStr = "Spades"
        return "{0} of {1}".format(rankStr, suitStr)

    def draw(self, win, center):
        filename = "./Playing_Card_Images/{0}{1}.png".format(
            self.rank, self.suit.upper())
        loadedCardImage = Image(center, filename)
        loadedCardImage.draw(win)


def main():
    print("Testing card class")
    n = 5
    win = GraphWin("Playing Card", 700, 900)
    win.setCoords(-10, -10, 10, 10)
    cardCenter = Point(0, 0)

    for i in range(n):
        rank = randrange(1, 14)
        suit = "dchs"[randrange(4)]
        randCard = PlayingCard(rank, suit)
        print(randCard, "counts", randCard.value())
        randCard.draw(win, cardCenter)
        win.getMouse()


if __name__ == '__main__':
    main()
