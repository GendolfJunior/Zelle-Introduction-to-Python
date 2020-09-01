#  6. Expand your soluation to the previous problem to allow the calcualtion of a complete name such as "John Marvin Zelle" or
#     "John Jacob Jingleheimer Smith." The total value is just the sum of the numberic values of all the names.
#

# create a string of alphabet
# take as an input from the user a complete name and make it lower case
# create a loop for the name
#   which will return index of the letter from the string alphabet
#   sum the index
# print the sum

def main():
    alpha = "abcdefghijklmnopqrstuvwxyz"
    name = input("Enter the name: ")
    name2 = name.lower().split()
    sum = 0
    for i in name2:
        for j in i:
            sum = sum + alpha.find(j) + 1

    print("The final sum of your {0} is {1}".format(name, sum))


main()
