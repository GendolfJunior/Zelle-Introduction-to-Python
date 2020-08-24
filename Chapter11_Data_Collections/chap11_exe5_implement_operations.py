# 5. Most languages do not have the flexible built-in list (array) operations
# that Python has. Write an algorithm for each of the following Python
# operations and test your algorithm by writing it up in a suitable function.
# For example, as a function, reverse(myList) should do the same as
# my List.reverse(). Obviously, you are not allowed to use the corresponding
# Python method to implement your function.

def count(list, x):
    # returns the number of occurances of x in the list
    counter = 0
    for i in list:
        if i == x:
            counter += 1
    return counter


def isin(list, x):
    inTheList = False
    if x in list:
        inTheList = True

    return inTheList


def index(list, x):
    position = 0
    for i in list:
        position += 1
        # print("position is:", position)
        if i == x:
            return position


def reverse(list):
    reversed = []
    for i in list:
        reversed.insert(0, i)
    return reversed


def sort(list):
    sorted = []
    for i in list:
        if len(sorted) == 0:
            sorted.append(i)                # add fitst element of the list
        elif i >= sorted[-1]:
            sorted.append(i)                # item is the biggest, so add this item as the last in the list
        else:
            position = -1
            positionValue = sorted[-1]      # get the last value in the sorted list
            while i < positionValue:        # loop through the sorted list comparing current value with list values
                position = position - 1
                if len(sorted) + position < 0:
                    break                       # exit if nothing left in the sorted list
                else:
                    positionValue = sorted[position]    # assign a new position to check against the current value
            sorted.insert(position + 1, i)   # insert the value in the sorted list after the item smaller than the current value
    return sorted


def main():
    data = [8, 2, 1, 5, 6, 1, 5, 3, 2, 2, 4]
    x = 5
    # print(count(data, x))
    # print(isin(data, x))
    # print(index(data, x))
    print(reverse(data))
    # print(sort(data))


if __name__ == '__main__':
    main()
