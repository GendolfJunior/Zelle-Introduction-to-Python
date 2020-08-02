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
# that results in a total between 17 and 21 inclusive; otherwise, the ace is
# counted as 1.
# Write a program that simulates multiple games of blackjack and estimates
# the probability that the dealer will bust. Hints: Treat the deck of
# cards as infinite (casinos use a "shoe" containing many decks). You do not
# need to keep track of the cards in the hand, just the total so far (treating
# an ace as 1) and a bool variable hasAce that tells whether or not the
# hand contains an ace. A hand containing an ace should have 10 points
# added to the total exactly when doing so would produce a stopping total
# (something between 17 and 21 inclusive).
from random import *


def getUserInputs():
    gamesCount = int(input("Enter how many games to simulate: "))
    return gamesCount


def getPlayCard():
    # this function randomly picks a card in the range from 6 to 14 (ace)
    cardNumb = randrange(6, 14)
    cards = {6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 10, 12: 10, 13: 10, 14: 11}
    score = cards.get(cardNumb)
    return score, cardNumb


def simulate1game():
    # Simulates a single game
    # Returns final scores for A and B
    totalScorePlayer = 0
    totalScoreDealer = 0
    while not gameOver(totalScorePlayer, totalScoreDealer):
        scorePlayer, cardnum = getPlayCard()
        if cardnum == 14:
            if (17 <= totalScorePlayer + scorePlayer <= 21):
                totalScorePlayer += scorePlayer
            else:
                totalScorePlayer += 1
        else:
            totalScorePlayer += scorePlayer

        scoreDealer, cardnum = getPlayCard()
        if cardnum == 14:
            if (17 <= totalScoreDealer + scoreDealer <= 21):
                totalScoreDealer += scoreDealer
            else:
                totalScoreDealer += 1
        else:
            totalScoreDealer += scoreDealer
        print(totalScorePlayer, totalScoreDealer)

    return totalScorePlayer, totalScoreDealer


def gameOver(a, b):
    # a and b represent scores for a racquetball game
    # Returns True if the game is over, False otherwise.
    return a >= 21 or b >= 21


def simulateNgames(games):
    # Simulates n games of blackjack between player and a dealer
    # Returns number of wins for A and B
    winsPlayer = winsDealer = 0
    for i in range(games):
        scorePlayer, scoreDealer = simulate1game()
        if scorePlayer <= 21 and scoreDealer <= 21:
            winsPlayer = winsPlayer + 1
            winsDealer = winsDealer + 1
        elif scorePlayer > 21 and scoreDealer > 21:
            pass
        elif scorePlayer <= 21 and scoreDealer > 21:
            winsPlayer = winsPlayer + 1
        else:
            winsDealer = winsDealer + 1
        print("in simulateNgames the wins are: ", winsPlayer, winsDealer)
    return winsPlayer, winsDealer


def printIntroBlackjack():
    print("this is a Blackjack simulation game")


def printReport(player, dealer, games):
    print("Player won: {0} games\nDealer won: {1} games".format(player, dealer))
    print("The estimated probabillity of a player win is {0:0.2%}".format(player / games))


def main():
    printIntroBlackjack()
    games = getUserInputs()
    player, dealer = simulateNgames(games)
    printReport(player, dealer, games)


if __name__ == '__main__':
    main()
