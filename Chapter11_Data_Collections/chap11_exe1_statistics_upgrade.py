# 1. Modify the statistics program from this chapter so that client programs
# have more flexibility in computing the mean and/ or standard deviation.
# Specifically, redesign the library to have the following functions:
# mean(nums) Returns the mean of numbers in nums.
# stdDev(nums) Returns the standard deviation of nums.
# meanStdDev(nums) Returns both the mean and standard deviation of nums.

# stats.py
from math import sqrt


def getNumbers():
    nums = []

    # sentinel loop to get numbers
    xStr = input("Enter a number (<Enter> to Quit) >>")
    while xStr != "":
        x = eval(xStr)
        nums.append(x)
        xStr = input("Enter a number (<Enter> to quit) >> ")
    return nums


def mean(nums):
    sum = 0.0
    for num in nums:
        sum = sum + num
    return sum / len(nums)


def stdDev(nums, xbar):
    sumDevSq = 0.0
    for num in nums:
        dev = xbar - num
        sumDevSq = sumDevSq + dev * dev
    return sqrt(sumDevSq / (len(nums) - 1))


def median(nums):
    nums.sort()
    size = len(nums)
    midPos = size // 2
    if size % 2 == 0:
        median = (nums[midPos] + nums[midPos - 1]) / 2
    else:
        median = nums[midPos]
    return median


def meanStdDev(nums):
    # Returns both the mean and standard deviation of nums.
    means = mean(nums)
    standDev = stdDev(nums, means)
    return means, standDev


def main():
    print("This program computes mean, median, and standard deviation.")

    data = getNumbers()
    data_mean, data_stDev = meanStdDev(data)
    med = median(data)

    print('\nThe mean is', data_mean)
    print("The standard deviation is", data_stDev)
    print("The median is", med)


if __name__ == '__main__': main()
