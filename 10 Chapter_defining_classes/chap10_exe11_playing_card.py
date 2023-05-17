# 11. Implement a class to represent a playing card. Your class should have the following methods:
# __init__ (self, rank, suit) rank is an int in the range 1-13 indicating
#       the ranks ace-king' and suit is a single character "d ' " "c' " "h ' " or "s"
#       indicating the suit (diamonds, clubs, hearts, or spades). Create the
#       corresponding card.
# getRank(self) Returns the rank of the card.
# get Suit (self) Returns the suit of the card.
# value(self) Returns the Blackjack value of a card. Ace counts as 1, face
#       cards count as 10.
# __str__ (self) Returns a string that names the card. For example, "Ace
#       of Spades".
# Note: A method named __str__ is special in Python. If asked to convert an
# object into a string, Python uses this method, if it's present. For example,
#           c = Card(l,"s")
#           print c
# will print 'Ace of Spades.'
# Test your card class with a program that prints out n randomly generated
# cards and the associated Blackjack value where n is a number supplied by the user.
from random import randrange


class PlayingCard:

    def __init__(self, rank, suit):
        self.rank = rank  # randrange(1, 13)
        self.suit = suit  # ["d", "c", "h", "s"]

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


def main():
    print("Testing card class")
    n = int(input("How many cards would you like to see? "))
    for i in range(n):
        rank = randrange(1, 14)
        suit = "dchs"[randrange(4)]
        randCard = PlayingCard(rank, suit)
        print(randCard, "counts", randCard.value())


if __name__ == '__main__':
    main()
