# 10. Do Programming Exercise 4 from Chapter 5 using a function acronym(phrase)
# that returns an acronym for a phrase supplied as a string.

def acronym(phrase):
    acronym = ""
    for a in phrase:
        acronym = acronym + a[0]
    return acronym


def main():
    phrase = input("Enter a phrase: ").split()
    print("\nThe acronym is: {0} ".format(acronym(phrase).upper()))


main()
