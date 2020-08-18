# 12. Modify the previous program to get its input from a file.

def fileInput(file):
    infile = open(file, 'r')
    data = []
    for line in infile:
        data.append(int(line))
    infile.close()
    return data


def measures(tempratures):
    heating, cooling = 0, 0
    for i in tempratures:
        #i = int(i)
        if i < 60:
            heating += 1
        elif i > 80:
            cooling += 1
        else:
            pass
    return heating, cooling


def main():
    print("this program calculates heating and cooling days!")
    file = input("Enter the filename: ")
    inputData = fileInput(file)
    heating, cooling = measures(inputData)
    print("There are {0} heating and {1} cooling days".format(heating, cooling))


if __name__ == '__main__':
    main()
