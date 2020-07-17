#  5. Numerologists claim to be able to determine a person's character traits based on the "numeric value" of a name. The value
#     of a name is determined by summing up the values of the letters of the name where "a" is 1, "b" is 2, "c" is 3, up to "z"
#     being 26. For example, the name "Zelle" would have the value 26 + 5 + 12 + 12 + 5 = 60 (which happens to be a very
#     auspicious number, by the way). Write a program that calculates the numeric value of a single name provided as input.
#

# create a string of alphabet
# take as an input from the user a name and make it lower case
# create a loop for the name
#   which will return index of the letter from the string alphabet
#   sum the index
# print the sum

def main():
    alpha = "abcdefghijklmnopqrstuvwxyz"
    name = input("Enter the name: ")
    nameLower = name.lower()
    sum = 0
    for i in nameLower:
        #print("the i is: ", i)
        sum = sum + alpha.find(i) + 1
        #print("the sum is: ", sum)

    print("The final sum of your {0} is {1}".format(name, sum))


main()
