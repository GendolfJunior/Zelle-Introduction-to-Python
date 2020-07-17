# 11. Write and test a function to meet this specification.
# squareEach (nums) nums is a list of numbers. Modifies the list by squaring each entry.

def squareEach(nums):
    # retunrs a list of squared numbers
    list = []
    for i in nums:
        list.append(i ** 2)
    return list


def main():
    nums = input("Enter the list of numbers, separated by comma: ")
    numbers = []
    for numString in nums.split(","):
        nums = float(numString)
        numbers.append(nums)

    print("The input list is: ", numbers)
    print("The output squared list is: ", squareEach(numbers))


main()
