# c09ex08.py
#    Simulation to Blackjack dealer to estimate bust probability.
# 8. Blackjack (twenty-one) is a casino game played with cards. The goal of the
# game is to draw cards that total as close to 21 points as possible without
# going over. All face cards count as 10 points, aces count as 1 or 11, and all
# other cards count their numeric value.
# The game is played against a dealer. The player tries to get closer to
# 21 (without going over) than the dealer. If the dealer busts (goes over
# 21), the player automatically wins (provided the player had not already
# busted). The dealer must always take cards according to a fixed set of
# rules. The dealer takes cards until he or she achieves a total of at least
# 17. If the dealer's hand contains an ace, it will be counted as 11 when
# that results in a total between 17 and 21 inclusive; otherwise, the ace is counted as 1.
# Write a program that simulates multiple games of blackjack and estimates
# the probability that the dealer will bust. Hints: Treat the deck of
# cards as infinite (casinos use a "shoe" containing many decks). You do not
# need to keep track of the cards in the hand, just the total so far (treating
# an ace as 1) and a bool variable hasAce that tells whether or not the
# hand contains an ace. A hand containing an ace should have 10 points
# added to the total exactly when doing so would produce a stopping total
# (something between 17 and 21 inclusive).

from random import randrange


def main():
    print("Simulation of a Blackjack dealer.\n")
    n = int(input("How many trials? "))
    busts = 0
    for i in range(n):
        points = dealHand()
        if points > 21:
            busts = busts + 1
    print("In %d hands dealer busted %d times." % (n, busts))
    print("Estimated prob =", float(busts) / n)


def dealHand():
    total = 0
    haveAce = False
    while total < 17:
        card = randrange(1, 14)
        if card == 1:
            haveAce = True
        total = total + BJValue(card)
        if haveAce:
            total = adjustForAce(total)
    return total


def BJValue(card):
    # this function assigns a real value to the card drawn from the deck
    if card > 10:
        return 10
    else:
        return card


def adjustForAce(total):
    if 16 < total + 10 < 22:
        return total + 10
    else:
        return total


if __name__ == '__main__':
    main()
