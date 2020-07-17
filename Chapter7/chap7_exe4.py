# 4. A certain college classifies students according to credits earned. A student
# with less than 7 credits is a Freshman. At least 7 credits are required to be
# a Sophomore, 16 to be a Junior and 26 to be classified as a Senior. Write a
# program that calculates class standing from the number of credits earned.

def main():
    print("College Classification\n")
    credits = float(input("Enter number of credits: "))
    if credits < 7:
        cls = "Freshman"
    elif credits < 16:
        cls = "Sophomore"
    elif credits < 26:
        cls = "Junior"
    else:
        cls = "Senior"
    print("The classification is", cls)

if __name__ == '__main__':
    main()