#  4. An acronym is a word formed by taking the first letters of the words in a phrase and making a word from them. For
#     example, RAM is an acronym for "random access memory." Write a program that allows the user to type in a phrase and
#     then outputs the acronym for that phrase. Note: The acronym should be all uppercase, even if the words in the phrase
#     are not capitalized.
#
#     Input: A string of words demarcated by spaces
#     Output: A string that is an acronym of the first letter of each word in the string
#
#     get user input
#     split user input on list of strings
#     use function title() function to capitalize first letter
#     loop over the list
#         add to a new string variable = variable + first index of a letter in the word
#     print the final string

def main():
    phrase = input("Enter a phrase: ").split()
    acronym = ""
    for a in phrase:
        acronym = acronym + a[0]

    print("\nThe acronym is: ")
    print(acronym.upper())


main()
