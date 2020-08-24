# c11ex05.py
# various list algorithms


def count(myList, x):
    ans = 0
    for item in myList:
        if item == x:
            ans = ans + 1
    return ans

def isin(myList, x):
    for item in myList:
        if item == x:
            return True
    return False

def index(myList, x):
    for i in range(len(myList)):
        if myList[i] == x:
            return i
    # If not found, raise a value error
    #   an alternative would be to return -1
    raise ValueError("x not in list")

# this solution from the book seems not working
def reverse(lst):
#    print('the len(lst)/2 = ', len(lst)/2)
    for i in range(int(len(lst)/2)):
#       print("i = ", i)
        j = -(i+1)
#        print("j = ", j)
        lst[i], lst[j] = lst[j], lst[i]
#       print("lst[i] = {0} and lst[j] = {1}".format(lst[i], lst[j]))
        return lst

def sort(lst):
    # selection sort. See Chapter 13 for other examples.
    for i in range(len(lst)-1):
        # find min of remaining items
        minpos = i
        print('i = ', i)
        for j in range(i+1, len(lst)):
            print("j = {0}, i+1 = {1}, len(lst) = {2}".format(j, i+1, len(lst)))
            if lst[j] < lst[minpos]:
                print("Evaluate lst[j] ({0}) < lst[minpos] ({1}), result {2}".format(lst[j], lst[minpos], lst[j] < lst[minpos]))
                minpos = j
                print("new minpos = ", minpos)
        # swap min to front of remaining
        lst[i], lst[minpos] = lst[minpos], lst[i]
    return lst

def main():
    # data = [8, 2, 1, 5, 6, 1, 5, 3, 2, 2, 4]
    data = [8, 2, 1, 5]
    x = 5
    # print(count(data, x))
    # print(isin(data, x))
    # print(index(data, x))
    # print(reverse(data))
    print(sort(data))


if __name__ == '__main__':
    main()
