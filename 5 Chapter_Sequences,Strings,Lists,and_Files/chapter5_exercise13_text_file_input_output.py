# 13. Redo any of the previous programming exercises to make them batch-oriented (using text files for input and output).

# print what is this program about
# get input of the key
# get input file name 1 for reading
# get input file name 2 for writting
# open the file 1 for reading
# open the file 2 for writting
# process each line of the text in the file
#   split the line on words
#   add each line to the list
# close the file for reading
# create a loop to go over each object in the list
# encrypt the object string using a formula chr(ord(ch) + key) and put it in another list
# write into another file
# print out the encoded list into the file
# close the file

def main():
    print(
        "This program gets the text from the input file\nencrypts it using the key you provide\nand writes encrypted messages in a separate file")

    # get inputs from a user
    encryptionKey = int(input("Enter the key: "))
    inFilename = input("Enter filename where to read a message? ")
    outFilename = input("Enter the filename where to write an encrypted message? ")

    # open the files
    infile = open(inFilename, 'r')
    outfile = open(outFilename, 'w', encoding="utf-8")

    sentences = []

    for line in infile:
        # print("the current value of line is: ", line)
        sentences += line.split()
        # print("the sentence currently is: ", sentences)

    sentences = "".join(sentences)
    enc_message = []

    for letter in sentences:
        enc_message.append(chr(ord(letter) + encryptionKey))
        # print("current enc message is: ", enc_message)

    final_message = "".join(enc_message)
    print("the final message is: ", final_message)
    print(final_message, file=outfile)
    infile.close()
    outfile.close()


main()
