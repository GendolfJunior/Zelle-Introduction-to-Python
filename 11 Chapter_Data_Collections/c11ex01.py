# c11ex01.py
#    Program to compute the mean, median, and standard deviation of
#    numbers entered interactively.

from math import sqrt


def getNumbers():
    nums = []  # start with an empty list

    # sentinel loop to get numbers
    xStr = input("Enter a number (<Enter> to quit) >> ")
    while xStr != "":
        x = float(xStr)
        nums.append(x)  # add this value to the list
        xStr = input("Enter a number (<Enter> to quit) >> ")
    return nums


def mean(nums):
    sum = 0.0
    for num in nums:
        sum = sum + num
    return sum / len(nums)


def meanStdDev(nums):
    xbar = mean(nums)
    sumDevSq = 0.0
    for num in nums:
        dev = num - xbar
        sumDevSq = sumDevSq + dev * dev
    return xbar, sqrt(sumDevSq / (len(nums) - 1))


def stdDev(nums):
    xbar, stdDev = meanStdDev(nums)
    return stdDev


def median(nums):
    nums.sort()
    size = len(nums)
    midPos = size // 2
    if size % 2 == 0:
        median = (nums[midPos] + nums[midPos - 1]) / 2
    else:
        median = nums[midPos]
    return median


def main():
    print('This program computes mean, median and standard deviation.')

    data = getNumbers()
    xbar, std = meanStdDev(data)
    med = median(data)

    print('\nThe mean is', xbar)
    print('The standard deviation is', std)
    print('The median is', med)


if __name__ == '__main__': main()
