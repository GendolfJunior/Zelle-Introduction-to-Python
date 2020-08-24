# searches.py
#    Implementation of linear and binary searches


def linSearch(x, nums):
    for i in range(len(nums)):
        if nums[i] == x:  # item found, return the index value
            return i
    return -1  # loop finished, item was not in list


def binSearch(x, nums):
    low = 0
    high = len(nums) - 1
    while low <= high:  # There is still a range to search
        mid = (low + high) // 2  # position of middle item
        item = nums[mid]
        if x == item:  # Found it! Return the index
            return mid
        elif x < item:  # x is in lower half of range
            high = mid - 1  # move top marker down
        else:  # x is in upper half
            low = mid + 1  # move bottom marker up
    return -1  # no range left to search, x is not there


def recBinSearch(x, nums, low, high):
    if low > high:  # No place left to look, return -1
        return -1
    mid = (low + high) // 2
    item = nums[mid]
    if item == x:  # Found it! Return the index
        return mid
    elif x < item:  # Look in lower half
        return recBinSearch(x, nums, low, mid - 1)
    else:  # Look in upper half
        return recBinSearch(x, nums, mid + 1, high)


def rbinSearch(x, nums):
    return recBinSearch(x, nums, 0, len(nums) - 1)


import random


# Simple test function. You can use this interactively to time different
#    size searches. Here's an example call:
#       >>> from searches import *
#       >>> avgTime(binSearch, 5000, 10)
#    This reports the average time needed to find a random value in a list
#    of 5000 ints. The average is done over 10 trials.

def avgTime(search, n, trials):
    # build an ordered list of size n
    l1 = list(range(n))
    print("List built")

    # run a number of trials and compute average time
    sum = 0.0
    for i in range(trials):
        print(i + 1, end=' ')  # show progress
        target = random.randint(0, n)
        # Get system time just before search
        t0 = time.time()
        pos = search(target, l1)
        # Get system time just after search
        t1 = time.time()
        # Add elapsed time to sum
        sum = sum + (t1 - t0)
    print("\naverage:", sum / trials)


import time

start_time = time.time()

from tkinter.filedialog import askopenfilename

def loadfile():
    #filename = askopenfilename()
    filename = "D:/Andriy/SelfDevelopment/Programming/Python/Zelle_Python_Intro/Chapter13_Algorithm_Design_Recursion/random_numbers.txt"
    infile = open(filename, 'r')
    data = []
    for i in infile.readlines():
        number = int(i)
        data.append(number)
    infile.close()
    return data

def main():
    # data = [1, 2, 5, 1, 3]
    x = 910013733
    data = loadfile()

    print(linSearch(x, data))


main()
print("%s seconds" % (time.time() - start_time))
