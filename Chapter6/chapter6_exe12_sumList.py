# 12. Write and test a function to meet this specification.
# sumList (nums) nums is a list of numbers. Returns the sum of the numbers in the list.

def convertString(string):
    # takes as input the string with float numbers, split by comma, appends the array list and returns it
    list = []
    for i in string.split(","):
        b = float(i)
        list.append(b)
    return list


def sumList(nums):
    sumNum = 0.0
    for i in nums:
        sumNum += i
    return sumNum


def main():
    someString = input("Enter the list of numbers: ")
    result = sumList(convertString(someString))

    print(result)


main()
