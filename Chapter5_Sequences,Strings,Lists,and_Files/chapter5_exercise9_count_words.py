# Write a program that counts the number of words in a sentence entered by the user.

# get input sentence from the user
# split the sentence into words with a default separator space
# create a list of values
# calculate a length of the list

def main():
    sentence = input("Enter a sentence: ").split()
    print("the list is: ", sentence)
    count = len(sentence)
    print("the length of the list is:", count)


main()