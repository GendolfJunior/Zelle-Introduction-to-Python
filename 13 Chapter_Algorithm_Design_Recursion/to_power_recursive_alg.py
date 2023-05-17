def recPower(a, n):
    # raises a to the int power n
    if n == 0:
        return 1
    else:
        factor = recPower(a, n // 2)
        if n % 2 == 0:  # n is even
            return factor * factor
        else:  # n is odd
            return factor * factor * a


import time

start_time = time.time()

#from tkinter.filedialog import askopenfilename

def loadfile():
    #filename = askopenfilename()
    filename = "D:/Andriy/SelfDevelopment/Programming/Python/Zelle_Python_Intro/13 Chapter_Algorithm_Design_Recursion/random_numbers.txt"
    infile = open(filename, 'r')
    data = []
    for i in infile.readlines():
        number = int(i)
        data.append(number)
    infile.close()
    return data

def main():
    # data = [1, 2, 5, 1, 3]
    x = 3
    n = 6
    #data = loadfile()
    print(recPower(x, n))  # 5 multiplications (checked in debug mode)

main()
print("%s seconds" % (time.time() - start_time))
