# 14.  use the functions from the previous 3 problems to implement a program that computes the sum of the squares of numbers
# read from a file. Your program should prompt for a file name and print out the sum of the squares of the values in the file.
# Hint: use readlines()

# Specification
#   1. get input filename with numbers
#   2. print out the sume of the squares

# Design
#   1. get filename and open it for reading, assume comma is a separator
#   2. readfile content into a variable list
#   3.

from tkinter.filedialog import askopenfilename


def file():
    # get the input filename and open it for reading
    inFilname = askopenfilename()
    infile = open(inFilname, 'r')
    return infile


def score(infile):
    # create a list of score values as integers
    scores = []
    for score in infile.readlines():
        scores.append(float(score[:-1]))
    scores.sort()
    print(scores)
    return scores


def squareEach(nums):
    # retunrs a list of squared numbers
    list = []
    for i in nums:
        list.append(i ** 2)
    return list


def sumList(nums):
    sumNum = 0.0
    for i in nums:
        sumNum += i
    return sumNum


def main():
    print("This program reads a file with scores, calculates a square of each score and sums it")
    infile = file()
    scores = score(infile)
    squared = squareEach(scores)
    squaredSum = sum(squared)
    print("the squared sum of numbers is: ", squaredSum)


main()
