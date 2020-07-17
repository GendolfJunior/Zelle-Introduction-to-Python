# 10. Write a program that calculates the average word length in a sentence entered by the user.

# get user input of the sentence
# split the sentence on words with a default separator space
# assign to a variable split of the sentence
# create a variable = 0 to hold a sum
# create a loop in through the list
#   take each list item and calculate it's length
#   sum = sum + length of the item
# divide sum on length of the list
# print the result

def main():
    sentence = input("Enter the sentence: ").split()
    print("the sentence is: ", sentence)
    listLength = len(sentence)
    sum = 0.0
    for i in sentence:
        sum = sum + len(i)
        print("current sum is: ", sum)
    result = sum / listLength
    print("the average word length is: ", result)

main()
