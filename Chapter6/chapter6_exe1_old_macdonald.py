# 1 Write a program to print the lyrics of the song "Old MacDonald." Your
# program should print the lyrics for five different animals, similar to the
# example verse below.

#   Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!
#   And on that farm he had a cow, Ee-igh, Ee-igh, Oh!
#   With a moo, moo here and a moo, moo there.
#   Here a moo, there a moo, everywhere a moo, moo.
#   Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!

# Implementation
# def main function
# create a a function that takes an animal as an input parameter
# and returns the text with that animal inserted
# pass 5 diferent
# print out what was returned by the function
def song(animal):
    print(
        "Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!\nAnd on that farm he had a {0}, Ee-igh, Ee-igh, Oh!\nWith a moo, moo here and a moo, moo there.\nHere a moo, there a moo, everywhere a moo, moo.\nOld MacDonald had a farm, Ee-igh, Ee-igh, Oh!\n".format(
            animal))


def main():
#    animal1, animal2, animal3, animal4, animal5 = eval(input("Enter a max of 5 animals using comma as a separator: "))
    animal1 = input("Enter first animal: ")
    animal2 = input("Enter first animal: ")
    animal3 = input("Enter first animal: ")
    animal4 = input("Enter first animal: ")
    animal5 = input("Enter first animal: ")

    song(animal1)
    song(animal2)
    song(animal3)
    song(animal4)
    song(animal5)


main()
