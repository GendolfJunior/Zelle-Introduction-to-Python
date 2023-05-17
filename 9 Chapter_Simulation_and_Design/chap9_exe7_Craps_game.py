# 7. Craps is a dice game played at many casinos. A player rolls a pair of normal
# six-sided dice. If the initial roll is 2, 3, or 12, the player loses. If the roll is
# 7 or 11, the player wins. Any other initial roll causes the player to "roll for
# point." That is, the player keeps rolling the dice until either rolling a 7 or
# re-rolling the value of the initial roll. If the player re-rolls the initial value
# before rolling a 7, it's a win. Rolling a 7 first is a loss.
# Write a program to simulate multiple games of craps and estimate the
# probability that the player wins. For example, if the player wins 249 out of
# 500 games, then the estimated probability of winning is 249/500 = 0.498.

# print intro
# function roll dice with random number generation as integer in the range 1 to 13 exclusive
# function games condition if the player rolls value 2,3,12 exit and record the

# c09ex07.py
#   Simulation of game of craps.

from random import randrange


def main():
    print("This program estimates the probability of winning at craps.")
    n = int(input("How many games should I simulate? "))
    wins = simNGames(n)
    print("\nThe player wins", wins, "games.")
    print("The estimated probabillity of a win is {0:0.2%}".format(wins / n))


def simNGames(n):
    wins = 0
    for i in range(n):
        if winCraps():
            wins = wins + 1
    return wins


def winCraps():
    roll = rollDice()
    if roll == 7 or roll == 11:
        return True
    elif roll == 2 or roll == 3 or roll == 12:
        return False
    else:
        return rollForPoint(roll)


def rollForPoint(toMake):
    roll = rollDice()
    while roll != 7 and roll != toMake:
        roll = rollDice()
    return roll == toMake


def rollDice():
    return randrange(1, 7) + randrange(1, 7)


if __name__ == '__main__':
    main()
