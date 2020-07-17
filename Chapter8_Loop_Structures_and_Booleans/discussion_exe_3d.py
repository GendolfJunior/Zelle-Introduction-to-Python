# d) The number of times a whole number n can be divided by 2 (using
# integer division) before reaching 1 (i.e., log2n) .

def main():
    n = int(input("Enter the number n to be divided: "))
    i = 2
    times = 0
    while ((n % i) == 0):
        i *= 2
        times += 1
    print("it could be divided {0} times".format(times))


main()
