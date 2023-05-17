# A simple program illustrating chaotic behavior.
# get input of 2 values in the range between 0 and 1
# get the number of iterations for in range loop into a variable
# print out formated header with inputed starting values
# for i in range iterations
#       calc for inputed X1
#       calc for inputed X2
#       print out resultY1
#       print out resultY2

def main():
    print("This program illustrates a chaotic function")
    x1, x2 = eval(input("Enter the values for X1 and X2 in the range 0 .. 1, separated by comma: "))
    iterations = int(input("Enter how many iterations to calculate the value should happen: "))

    print("index {0:6.2f} {1:9.2f}".format(x1, x2))
    print("-------------------------")

    index = 0

    for i in range(iterations):
        index += i
        x1 = 3.9 * x1 * (1 - x1)
        x2 = 3.9 * x2 * (1 - x2)
        print("{0:3} {1:10.7f} {2:10.7f}".format(index, x1, x2))


main()
