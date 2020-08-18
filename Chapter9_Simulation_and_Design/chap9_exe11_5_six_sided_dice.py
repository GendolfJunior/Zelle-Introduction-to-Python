# 11. Write a program that performs a simulation to estimate the probability of
# rolling five of a kind in a single roll of five six-sided dice.

from random import randrange


def main():
    print("This program estimates the probability of winning at craps with 5 dices.")
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
    roll = 0
    for dice in range(1, 6):
        roll += randrange(1, 7)
        print(roll)
    print("the final roll is: ", roll)
    return roll/5

if __name__ == '__main__':
    main()
