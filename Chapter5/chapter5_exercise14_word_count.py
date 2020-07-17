# 14. Word Count. A common utility on Unix/Linux systems is a small program called "wc." This program analyzes a file to determine the
#     number of lines, words and characters contained therein. Write your own verison of wc. The program should accept a file name as
#     input and then print three numbers showing the count of lines, words, and characters in the file.

# get from a use the input filename to read from
# assign the filename to a variable and open the file for reading
# readlines() into a variable and then use len to calculate how many there
# take each line in the loop
#   inside each line create another loop with split()
#   default split is 'space'
#   create a list variable and assign there every word
# calculate the length of the list
#

def main():
    print(
        "This program gets the text from the input file\nencrypts it using the key you provide\nand writes encrypted messages in a separate file")

    # get filename from a user as input and open it for reading
    inFilename = input("Enter filename where to read a message? ")
    infile = open(inFilename, 'r')
    lines_count = 0
    words_count = 0
    letters_count = 0

    for line in infile:
        lines_count = lines_count + 1
        line_list = len(line.split())
        words_count = words_count + line_list
        letters_count = letters_count + len(line)
    print("There are:\n{0} lines\n{1} words\nand {2} letters\nin this file ".format(lines_count, words_count, letters_count))

    infile.close()


main()
