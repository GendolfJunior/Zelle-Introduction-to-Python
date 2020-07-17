# 13 write and test function to meet this specification
# toNumbers(strList) str:ist is a list of strings, each of which represents a number. Modiifes each entry in the list by converting it to a number

def toNumbers(strList):
    list = []
    for i in strList.split(','):
        list.append(float(i))
    return list

def main():
    print("Enter the list of numbers using comma as a separator")
    strList = (input("your numbers go here: "))
    print(toNumbers(strList))
    strList = toNumbers(strList)
    newList = strList[0] + strList[2]
    print(newList)


main()